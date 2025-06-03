# download_yolov5s.py
import urllib.request
import os

# 저장 경로 생성
os.makedirs("./models", exist_ok=True)

# 다운로드 URL
url = "https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.onnx"
save_path = "./models/yolov5s.onnx"

try:
    print("🔽 YOLOv5s ONNX 모델 다운로드 중...")
    urllib.request.urlretrieve(url, save_path)
    print("✅ 다운로드 완료:", save_path)
except Exception as e:
    print("❌ 다운로드 실패:", e)
