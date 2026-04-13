import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    """Test GET / — Thông tin giới thiệu hệ thống"""
    res = requests.get(f"{BASE_URL}/", timeout=10)
    print("=== GET / ===")
    print("Status:", res.status_code)
    print("Response:", res.json())
    print()

def test_health():
    """Test GET /health — Kiểm tra trạng thái"""
    res = requests.get(f"{BASE_URL}/health", timeout=10)
    print("=== GET /health ===")
    print("Status:", res.status_code)
    print("Response:", res.json())
    print()

def test_predict_positive():
    """Test POST /predict — Review tích cực (tiếng Anh)"""
    payload = {"text": "This food is really excellent, I love it!"}
    res = requests.post(f"{BASE_URL}/predict", json=payload, timeout=30)
    print("=== POST /predict (positive - EN) ===")
    print("Input:", payload["text"])
    print("Status:", res.status_code)
    print("Response:", res.json())
    print()

def test_predict_negative():
    """Test POST /predict — Review tiêu cực (tiếng Anh)"""
    payload = {"text": "Terrible food, worst experience ever. Never coming back."}
    res = requests.post(f"{BASE_URL}/predict", json=payload, timeout=30)
    print("=== POST /predict (negative - EN) ===")
    print("Input:", payload["text"])
    print("Status:", res.status_code)
    print("Response:", res.json())
    print()

def test_predict_neutral():
    """Test POST /predict — Review trung lập (tiếng Việt)"""
    payload = {"text": "Món ăn bình thường, không có gì đặc biệt."}
    res = requests.post(f"{BASE_URL}/predict", json=payload, timeout=30)
    print("=== POST /predict (neutral - VI) ===")
    print("Input:", payload["text"])
    print("Status:", res.status_code)
    print("Response:", res.json())
    print()

def test_predict_empty():
    """Test POST /predict — Input rỗng (expect lỗi 422)"""
    payload = {"text": ""}
    res = requests.post(f"{BASE_URL}/predict", json=payload, timeout=30)
    print("=== POST /predict (empty input) ===")
    print("Status:", res.status_code)
    print("Response:", res.json())
    print()

def test_predict_missing_field():
    """Test POST /predict — Thiếu field (expect lỗi 422)"""
    payload = {}
    res = requests.post(f"{BASE_URL}/predict", json=payload, timeout=30)
    print("=== POST /predict (missing field) ===")
    print("Status:", res.status_code)
    print("Response:", res.json())
    print()


if __name__ == "__main__":
    test_root()
    test_health()
    test_predict_positive()
    test_predict_negative()
    test_predict_neutral()
    test_predict_empty()
    test_predict_missing_field()