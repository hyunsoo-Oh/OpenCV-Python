import cv2
import numpy as np

# 🔹 BGR 이미지 불러오기
img = cv2.imread("./resources/Lane.jpeg")
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 🔸 1. HSV 색공간으로 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 🔸 2. 색상 범위 정의
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 25, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# 🔸 3. 각 색상 범위 마스크 생성
mask_white = cv2.inRange(hsv, lower_white, upper_white)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# 🔸 4. 마스크 결합
mask_combined = cv2.bitwise_or(mask_white, mask_yellow)

# 🔸 5. 마스크 적용 (원본 이미지와 AND 연산)
result = cv2.bitwise_and(img, img, mask=mask_combined)

# 🔸 6. 결과 출력
cv2.imshow("Original", img)
cv2.imshow("Mask (White + Yellow)", mask_combined)
cv2.imshow("Masked Result", result)

# 🔸 7. 결과 저장
cv2.imwrite("./resources/lane_mask.jpeg", mask_combined)
cv2.imwrite("./resources/lane_result.jpeg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
