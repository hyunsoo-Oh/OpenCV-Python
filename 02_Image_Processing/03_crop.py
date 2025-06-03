import cv2

# 이미지 읽기
img = cv2.imread("./resources/image.webp")
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 이미지 크기 확인
h, w, _ = img.shape
print(f"이미지 크기: {w} x {h}")

# ROI 영역 설정 (중앙 200x200 영역) -> 특정 영역 추출 및 필터 적용용
x_start = w // 2 - 100
y_start = h // 2 - 100
roi = img[y_start:y_start+200, x_start:x_start+200]

# 결과 출력
cv2.imshow("Original", img)
cv2.imshow("Cropped ROI", roi)

# 저장
cv2.imwrite("./resources/cropped_roi.webp", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
