import cv2
import numpy as np

# 🔹 이미지 읽기
img = cv2.imread("./resources/Lane.jpeg")
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 🔸 HSV 색공간 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 🔸 흰색 + 노란색 마스크 정의
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 25, 255])
mask_white = cv2.inRange(hsv, lower_white, upper_white)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# 🔸 마스크 결합
mask_combined = cv2.bitwise_or(mask_white, mask_yellow)

# 🔸 관심영역(ROI) 설정 - 하단 절반 영역만 사용
height, width = mask_combined.shape
roi = np.zeros_like(mask_combined)

# 하단 절반에만 흰색(255) 채움 → 나머지는 0으로 남음
roi[height//2:, :] = 255

# 🔸 ROI와 마스크를 AND 연산하여 적용
masked_roi = cv2.bitwise_and(mask_combined, roi)

# 🔸 원본 이미지에도 마스크 적용
result = cv2.bitwise_and(img, img, mask=masked_roi)

# 🔸 결과 출력
cv2.imshow("Original", img)
cv2.imshow("Mask (White + Yellow)", mask_combined)
cv2.imshow("ROI Applied", masked_roi)
cv2.imshow("Masked Result with ROI", result)

# 🔸 저장
cv2.imwrite("./resources/lane_mask_roi.jpeg", masked_roi)
cv2.imwrite("./resources/lane_result_roi.jpeg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
