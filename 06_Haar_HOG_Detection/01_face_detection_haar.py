# 01_face_detection_haar.py
# 📌 Haar Cascade를 이용한 얼굴 검출 예제

import cv2

# [1] 얼굴 검출용 Haar Cascade 분류기 로드
# cv2.data.haarcascades는 OpenCV에서 제공하는 XML 분류기 경로
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# [2] 이미지 불러오기
# 실습 기준 경로는 항상 ./resources/image.webp 로 고정
img = cv2.imread("./resources/Upimage.jpeg")

# [3] 이미지가 정상적으로 불러와졌는지 확인
if img is None:
    print("❌ 이미지 로드 실패: ./resources/Upimage.jpeg 파일을 확인하세요.")
    exit()

# [4] 이미지 → 그레이스케일 변환 (얼굴 검출에 필요한 전처리)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# [5] detectMultiScale()로 얼굴 영역 검출
# - scaleFactor: 이미지 피라미드 크기 조절 비율 (1.1이면 10%씩 축소)
# - minNeighbors: 양성으로 간주하기 위한 최소 이웃 수 (값이 클수록 정확도 ↑, 검출 ↓)
# - minSize: 검출할 최소 객체 크기
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=5,
    minSize=(30, 30)
)

# [6] 검출된 얼굴 위치에 사각형 그리기
for (x, y, w, h) in faces:
    # (x, y): 좌상단 좌표, (w, h): 폭과 높이
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# [7] 결과 이미지 출력
cv2.imshow("Face Detection - Haar", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
