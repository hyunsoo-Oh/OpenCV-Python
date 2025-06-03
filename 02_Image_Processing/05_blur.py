import cv2

# 이미지 읽기
img = cv2.imread("./resources/image.webp")
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 평균 블러 (커널 크기 5x5)
blur_avg = cv2.blur(img, (5, 5))

# 가우시안 블러 (커널 크기 5x5, 표준편차 자동 계산)
blur_gauss = cv2.GaussianBlur(img, (5, 5), 0)

# 출력
cv2.imshow("Original", img)
cv2.imshow("Average Blur", blur_avg)
cv2.imshow("Gaussian Blur", blur_gauss)

# 저장
cv2.imwrite("./resources/blur_avg.webp", blur_avg)
cv2.imwrite("./resources/blur_gauss.webp", blur_gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
