import cv2

# 이미지 읽기
img = cv2.imread("./resources/image.webp")
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 1. 절대 크기 설정 (width=200, height=300) -> 정확히 640×480으로 맞춰야 할 때
resized_abs = cv2.resize(img, (200, 300), interpolation=cv2.INTER_LINEAR)

# 2. 비율 설정 (가로 0.5배, 세로 0.5배) -> 원본의 절반/2배 등 상대적 조절이 필요할 때
resized_scale = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 출력
cv2.imshow("Original", img)
cv2.imshow("Resized - Absolute", resized_abs)
cv2.imshow("Resized - Scale", resized_scale)

# 저장
cv2.imwrite("./resources/resized_abs.webp", resized_abs)
cv2.imwrite("./resources/resized_scale.webp", resized_scale)

cv2.waitKey(0)
cv2.destroyAllWindows()
