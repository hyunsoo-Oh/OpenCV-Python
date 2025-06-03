import cv2

# 이미지 읽기
img = cv2.imread("./resources/image.webp")
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# BGR → Grayscale 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR → HSV 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 이미지 출력
cv2.imshow("Original - BGR", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)

# 저장
cv2.imwrite("./resources/gray_output.webp", gray)
cv2.imwrite("./resources/hsv_output.webp", hsv)

# 키 입력 대기 후 종료
cv2.waitKey(0)
cv2.destroyAllWindows()
