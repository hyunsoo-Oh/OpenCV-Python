import cv2

# 이미지 읽기
img = cv2.imread("./resources/image.webp")  # 파일 경로에 맞게 변경

# 이미지 출력
cv2.imshow("My Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 그레이스케일 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 저장
cv2.imwrite("./resources/gray_output.jpg", gray)
