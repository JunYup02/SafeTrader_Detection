"""
Convert difraud_data (.jsonl files split across category folders) into a single CSV file.

Directory layout expected under DATA_DIR:
    difraud_data/
        fake_news/
            train.jsonl
            test.jsonl
            validation.jsonl
        job_scams/
            ...
        phishing/
            ...
        sms/
            ...
        political_statements/   <- excluded
        product_reviews/        <- excluded
        twitter_rumours/        <- excluded

Each .jsonl record contains "text" and "label" fields.
The output CSV adds "category" (folder name) and "split" (train/test/validation)
columns so the original source of each row can be traced.
"""

import csv
import json
from pathlib import Path

# Directory containing the category folders
DATA_DIR = Path(__file__).parent / "difraud_data"

# Output CSV file path
OUTPUT_FILE = Path(__file__).parent / "difraud_data.csv"

# Folders to skip when building the CSV
EXCLUDED_CATEGORIES = {"political_statements", "product_reviews", "twitter_rumours"}

# Expected split file names inside each category folder
SPLITS = ("train", "test", "validation")


def main():
    # Collect every category folder that is not excluded
    category_dirs = sorted(
        d for d in DATA_DIR.iterdir()
        if d.is_dir() and d.name not in EXCLUDED_CATEGORIES
    )

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as out_f:
        writer = csv.writer(out_f)
        writer.writerow(["category", "split", "text", "label"])

        for category_dir in category_dirs:
            category = category_dir.name

            for split in SPLITS:
                jsonl_path = category_dir / f"{split}.jsonl"
                if not jsonl_path.exists():
                    continue

                with jsonl_path.open("r", encoding="utf-8") as in_f:
                    for line in in_f:
                        line = line.strip()
                        if not line:
                            continue

                        record = json.loads(line)
                        writer.writerow([category, split, record.get("text"), record.get("label")])

    print(f"Saved combined CSV to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
