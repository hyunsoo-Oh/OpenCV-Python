import cv2

# 🔹 Grayscale 이미지 불러오기
img = cv2.imread("./resources/image.webp", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 🔸 Canny Edge Detection
# - 첫 번째 인자: 하위 임계값 (edge로 처리할 최소 경계 강도)
# - 두 번째 인자: 상위 임계값 (강한 edge)
# → 약한 에지는 상위 임계값과 연결될 때만 edge로 인정됨 (hysteresis 방식)
edges = cv2.Canny(img, 100, 200)

# 🔸 결과 출력
cv2.imshow("Original", img)
cv2.imshow("Canny Edge", edges)

# 🔸 결과 저장
cv2.imwrite("./resources/canny_edges.webp", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
