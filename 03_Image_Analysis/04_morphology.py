import cv2
import numpy as np

# 🔹 Grayscale 이미지 읽기
img = cv2.imread("./resources/image.webp", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 🔸 이진화 처리 (Otsu 이용)
_, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 🔹 커널 정의 (모양과 크기 설정 가능)
kernel = np.ones((5, 5), np.uint8)

# 1. 침식 (Erosion) → 흰 영역 축소
eroded = cv2.erode(binary, kernel, iterations=1)

# 2. 팽창 (Dilation) → 흰 영역 확장
dilated = cv2.dilate(binary, kernel, iterations=1)

# 3. 열림 (Opening) = 침식 후 팽창 → 작은 잡음 제거
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# 4. 닫힘 (Closing) = 팽창 후 침식 → 구멍/틈 메우기
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# 🔸 결과 출력
cv2.imshow("Original Binary", binary)
cv2.imshow("Eroded", eroded)
cv2.imshow("Dilated", dilated)
cv2.imshow("Opened (Noise Removed)", opened)
cv2.imshow("Closed (Hole Filled)", closed)

# 🔸 결과 저장
cv2.imwrite("./resources/morph_eroded.webp", eroded)
cv2.imwrite("./resources/morph_dilated.webp", dilated)
cv2.imwrite("./resources/morph_opened.webp", opened)
cv2.imwrite("./resources/morph_closed.webp", closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
