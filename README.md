# Food Review Sentiment API

## 1. Thông tin sinh viên
- **Họ tên:** Đặng Quang Huy
- **MSSV:** 24120322
- **Lớp:** 24CTT3
- **Môn:** Tư Duy Tính Toán

## 2. Mô hình Hugging Face
- **Model:** `nlptown/bert-base-multilingual-uncased-sentiment`
- **Link:** [https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)

## 3. Mô tả hệ thống
API sử dụng **FastAPI** để nhận câu review văn bản về món ăn, gọi mô hình BERT multilingual từ Hugging Face để phân tích cảm xúc, và trả về kết quả sentiment theo thang **1–5 sao** ở dạng JSON.

**Các chức năng chính:**
- Phân tích cảm xúc review món ăn (hỗ trợ đa ngôn ngữ: Tiếng Anh, Tiếng Việt, ...)
- Trả về rating (1-5 sao), ý nghĩa, và độ tin cậy (confidence)
- Kiểm tra dữ liệu đầu vào và xử lý lỗi

## 4. Cài đặt thư viện

### Yêu cầu
- Python 3.10+

### Các bước cài đặt

```bash
# Clone repository
git clone https://github.com/<username>/food-review-sentiment-api.git
cd food-review-sentiment-api

# Tạo virtual environment
python -m venv .venv

# Kích hoạt virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Cài đặt thư viện
pip install -r requirements.txt
```

## 5. Hướng dẫn chạy chương trình

```bash
# Kích hoạt virtual environment (nếu chưa)
.\.venv\Scripts\activate

# Chạy server
uvicorn main:app --reload
```

Server sẽ chạy tại: `http://127.0.0.1:8000`

Truy cập Swagger UI (tài liệu API tự động): `http://127.0.0.1:8000/docs`

## 6. Hướng dẫn gọi API

### 6.1. GET / — Thông tin hệ thống

**Request:**
```bash
curl http://127.0.0.1:8000/
```

**Response:**
```json
{
  "message": "API đánh giá cảm xúc review món ăn (1-5 sao)"
}
```

---

### 6.2. GET /health — Kiểm tra trạng thái

**Request:**
```bash
curl http://127.0.0.1:8000/health
```

**Response:**
```json
{
  "status": "OK"
}
```

---

### 6.3. POST /predict — Phân tích cảm xúc

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This food is really excellent, I love it!"}'
```

Hoặc bằng Python:
```python
import requests

url = "http://127.0.0.1:8000/predict"
payload = {"text": "This food is really excellent, I love it!"}
res = requests.post(url, json=payload, timeout=30)
print(res.json())
```

**Response (review tích cực):**
```json
{
  "input": "This food is really excellent, I love it!",
  "output": {
    "rating": "5 stars",
    "meaning": "Rất ngon",
    "confidence": 0.9616
  }
}
```

**Response (review tiêu cực):**
```json
{
  "input": "Terrible food, worst experience ever. Never coming back.",
  "output": {
    "rating": "1 star",
    "meaning": "Rất dở",
    "confidence": 0.9684
  }
}
```

**Response (lỗi — thiếu dữ liệu):**
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "text"],
      "msg": "Field required",
      "input": {}
    }
  ]
}
```

## 7. Chạy kiểm thử API

```bash
# Đảm bảo server đang chạy ở terminal khác
python test_api.py
```

File `test_api.py` sẽ tự động kiểm thử 7 test cases:
1. `GET /` — Thông tin hệ thống
2. `GET /health` — Kiểm tra trạng thái
3. `POST /predict` — Review tích cực (tiếng Anh)
4. `POST /predict` — Review tiêu cực (tiếng Anh)
5. `POST /predict` — Review trung lập (tiếng Việt)
6. `POST /predict` — Input rỗng (expect lỗi 422)
7. `POST /predict` — Thiếu field (expect lỗi 422)

## 8. Cấu trúc dự án

```
food-review-sentiment-api/
├── main.py              # FastAPI application (endpoints)
├── model.py             # Sentiment classification model
├── config.yaml          # Cấu hình model path
├── test_api.py          # Script kiểm thử API
├── requirements.txt     # Danh sách thư viện
└── README.md            # Tài liệu dự án
```

## 9. Video Demo



https://github.com/user-attachments/assets/c7322a17-28e0-4572-9d77-e6e3eaf8ea88


