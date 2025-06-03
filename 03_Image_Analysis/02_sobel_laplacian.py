import cv2
import numpy as np

# 🔹 그레이스케일 이미지 불러오기
img = cv2.imread("./resources/image.webp", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 1. Sobel 연산 - x방향 (수직 에지 검출)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # dx=1, dy=0
sobel_x = cv2.convertScaleAbs(sobel_x)  # 절댓값 → 8bit로 변환

# 2. Sobel 연산 - y방향 (수평 에지 검출)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # dx=0, dy=1
sobel_y = cv2.convertScaleAbs(sobel_y)

# 3. Sobel 결과 결합
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# 4. Laplacian 연산 - 2차 미분 기반 전체 에지 검출
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

# 🔸 결과 출력
cv2.imshow("Original", img)
cv2.imshow("Sobel X (Vertical Edges)", sobel_x)
cv2.imshow("Sobel Y (Horizontal Edges)", sobel_y)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.imshow("Laplacian", laplacian)

# 🔸 결과 저장
cv2.imwrite("./resources/sobel_x.webp", sobel_x)
cv2.imwrite("./resources/sobel_y.webp", sobel_y)
cv2.imwrite("./resources/sobel_combined.webp", sobel_combined)
cv2.imwrite("./resources/laplacian.webp", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
