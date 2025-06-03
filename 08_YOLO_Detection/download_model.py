import os
import urllib.request
import ssl

# SSL 인증서 문제 방지 (일부 macOS 환경에서 필요)
ssl._create_default_https_context = ssl._create_unverified_context

def download_file(url, filepath, description="파일"):
    """파일 다운로드 함수"""
    try:
        if os.path.exists(filepath):
            print(f"✅ 이미 존재함: {filepath}")
            return True

        print(f"🔽 다운로드 중: {description}")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())

        print(f"✅ 다운로드 완료: {filepath}")
        return True

    except Exception as e:
        print(f"❌ 다운로드 실패: {filepath} - {e}")
        return False

def main():
    os.makedirs("./08_YOLO_Detection/models", exist_ok=True)

    # YOLOv3-tiny 구성 및 가중치 파일
    files_to_download = [
        {
            "url": "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg",
            "path": "./08_YOLO_Detection/models/yolov3-tiny.cfg",
            "desc": "YOLOv3-tiny 구조 파일"
        },
        {
            "url": "https://pjreddie.com/media/files/yolov3-tiny.weights",
            "path": "./08_YOLO_Detection/models/yolov3-tiny.weights",
            "desc": "YOLOv3-tiny 가중치 파일"
        },
        {
            "url": "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names",
            "path": "./08_YOLO_Detection/models/coco.names",
            "desc": "COCO 클래스 이름 파일"
        }
    ]

    print("📦 YOLOv3-tiny 모델 및 클래스 목록 다운로드 시작...\n")
    for item in files_to_download:
        download_file(item["url"], item["path"], item["desc"])

    print("\n🎉 모든 파일 다운로드 완료!")

if __name__ == "__main__":
    main()
