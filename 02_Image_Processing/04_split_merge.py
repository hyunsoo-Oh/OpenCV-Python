import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread("./resources/image.webp")
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 채널 분리
b, g, r = cv2.split(img)

# 단일 채널을 컬러 이미지처럼 보기 위해 병합 (다른 채널은 0으로 채움)
zeros = np.zeros_like(b)
blue_img = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img = cv2.merge([zeros, zeros, r])

# 채널 병합 → 원본 복원
merged = cv2.merge([b, g, r])

# 출력
cv2.imshow("Original", img)
cv2.imshow("Blue Channel", blue_img)
cv2.imshow("Green Channel", green_img)
cv2.imshow("Red Channel", red_img)
cv2.imshow("Merged", merged)

# 저장
cv2.imwrite("./resources/blue_channel.webp", blue_img)
cv2.imwrite("./resources/green_channel.webp", green_img)
cv2.imwrite("./resources/red_channel.webp", red_img)
cv2.imwrite("./resources/merged.webp", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
