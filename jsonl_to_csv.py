"""
datasets/difraud_data 폴더 안의 .jsonl 파일들을
동일한 폴더 구조를 유지한 채 datasets/difraud_data_csv 폴더에 .csv로 변환하는 스크립트

예)
datasets/difraud_data/phishing/train.jsonl
  -> datasets/difraud_data_csv/phishing/train.csv
"""

import json
import csv
from pathlib import Path

# 원본 데이터가 있는 폴더와, 결과를 저장할 폴더 경로 설정
SOURCE_DIR = Path("datasets/difraud_data")
TARGET_DIR = Path("datasets/difraud_data_csv")


def convert_jsonl_to_csv(jsonl_path: Path, csv_path: Path) -> None:
    """jsonl 파일 하나를 읽어서 csv 파일 하나로 변환하는 함수"""

    # jsonl 파일을 한 줄씩 읽어서 딕셔너리 리스트로 변환
    rows = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:  # 빈 줄은 건너뜀
                continue
            rows.append(json.loads(line))

    if not rows:  # 내용이 없는 파일이면 변환하지 않고 종료
        return

    # 파일마다 컬럼(키) 구성이 다를 수 있으므로,
    # 모든 줄에 등장하는 키를 모아서 csv 헤더로 사용
    fieldnames = []
    for row in rows:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    # 변환된 csv를 저장할 폴더가 없으면 생성
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    # csv 파일로 저장
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"변환 완료: {jsonl_path} -> {csv_path}")


def main() -> None:
    # SOURCE_DIR 안의 모든 .jsonl 파일을 재귀적으로 탐색
    jsonl_files = sorted(SOURCE_DIR.rglob("*.jsonl"))

    if not jsonl_files:
        print(f"{SOURCE_DIR} 안에서 .jsonl 파일을 찾지 못했습니다.")
        return

    for jsonl_path in jsonl_files:
        # SOURCE_DIR 기준 상대 경로를 구해서 TARGET_DIR에 동일한 구조로 매핑
        relative_path = jsonl_path.relative_to(SOURCE_DIR)
        csv_path = TARGET_DIR / relative_path.with_suffix(".csv")

        convert_jsonl_to_csv(jsonl_path, csv_path)


if __name__ == "__main__":
    main()