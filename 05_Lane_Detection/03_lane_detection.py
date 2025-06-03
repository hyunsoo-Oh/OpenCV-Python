import cv2
import numpy as np

# 🔹 이미지 읽기
img = cv2.imread("./resources/Lane.jpeg")
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# HSV 변환 및 색상 마스킹 (흰색 + 노란색)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 25, 255])
mask_white = cv2.inRange(hsv, lower_white, upper_white)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

mask = cv2.bitwise_or(mask_white, mask_yellow)

# ROI 설정 (하단 영역만 사용)
height, width = mask.shape
roi = np.zeros_like(mask)
roi[height//2:, :] = 255  # 하단 절반만 활성화
mask_roi = cv2.bitwise_and(mask, roi)

blur = cv2.GaussianBlur(mask_roi, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# 🔸 Canny 에지 검출
edges = cv2.Canny(mask_roi, 50, 150)

# 🔸 Hough Line 검출
lines = cv2.HoughLinesP(
    edges,                  # 입력 이미지 (에지)
    rho=1,                  # 거리 해상도 (픽셀)
    theta=np.pi / 180,      # 각도 해상도 (라디안)
    threshold=30,           # 최소 투표 수 (적을수록 더 많이 감지)
    minLineLength=50,       # 최소 선 길이
    maxLineGap=100          # 선 사이의 최대 간격
)

# 🔸 선분 그리기
line_img = img.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 1)

# 🔸 결과 출력
cv2.imshow("Original", img)
cv2.imshow("Edges (Canny)", edges)
cv2.imshow("Detected Lanes", line_img)
print(f"🔍 검출된 선 개수: {len(lines) if lines is not None else 0}")

# 🔸 저장
cv2.imwrite("./resources/lane_edges.jpeg", edges)
cv2.imwrite("./resources/lane_detected.jpeg", line_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
