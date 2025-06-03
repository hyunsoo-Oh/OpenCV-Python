# 02_people_detection_hog.py
# 📌 HOG + SVM을 이용한 사람(보행자) 검출 실습

import cv2

# [1] 기본 HOG + SVM 기반 사람 검출기 생성
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# [2] 이미지 불러오기
img = cv2.imread("./resources/streetp.jpeg")
if img is None:
    print("❌ 이미지 로드 실패")
    exit()

# [3] 사람 검출
# - winStride: 검색 윈도우 이동 간격 (속도-정확도 트레이드오프)
# - padding: 경계 여유 공간
# - scale: 이미지 피라미드 축소 비율
boxes, weights = hog.detectMultiScale(
    img,
    winStride=(4, 4),      # 기본값보다 촘촘하게
    padding=(8, 8),        # 테두리 여유 줄이기
    scale=1.03             # 더 작은 인물까지 탐색
)

# [4] 검출된 영역 그리기
for (x, y, w, h) in boxes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

# [5] 결과 출력
cv2.imshow("People Detection - HOG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
