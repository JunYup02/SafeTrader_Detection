# 🚩 Green Flag

**ML 기반 중고거래(C2C) 사기 탐지 Chrome 확장 프로그램**

중고거래 게시글을 보면, 구매 전에 사기 확률과 이유를 알려주는 서비스를 만듭니다.

## 무엇을 할 것인가

- 게시글 텍스트 + 판매자/구매자/거래 정보를 분석해 **사기 확률(%)** 을 계산
- 텍스트 모델 + 구조화 데이터 모델을 **가중 앙상블**로 결합 (텍스트 60% : 구조화 40%)
- Chrome 확장 프로그램으로 거래 페이지에 **위험도와 근거**를 바로 표시
- 목표 성능: **F1-score ≥ 0.90**

## 왜 하는가

C2C 중고거래는 결제 보호도, 판매자 검증도, 사전 경고도 없어 사기에 취약합니다. 돈을 잃고 나서가 아니라 **거래 전에** 경고하는 것이 목표입니다.

## 데이터

- `datasets/Fraudulent_E-Commerce_Transaction_Data/Fraudulent_E-Commerce_Transaction_Data.csv`는 375MB로 GitHub 파일 용량 제한(100MB)을 초과해 저장소에 포함되어 있지 않습니다. [Kaggle](https://www.kaggle.com/datasets/shriyashjagtap/fraudulent-e-commerce-transactions)에서 별도로 다운로드해 같은 경로에 넣어주세요.
- `datasets/difraud_data_csv/`는 `jsonl_to_csv.py`로 `datasets/difraud_data/`(원본 jsonl)를 변환해 생성합니다.
- `*_cleaned.csv` 파일들은 `EDA_text.ipynb`, `EDA_struc.ipynb`를 실행하면 재생성됩니다.

## 실행 환경

```bash
pip install -r requirements.txt
```

## Team D · 2026.07