import cv2

# 🔹 카메라 초기화
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# 실제 설정 값 확인
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

# 🔸 VideoWriter 초기화
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./resources/output_processed.avi', fourcc, fps, (width, height), isColor=False)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 🔸 1. Grayscale 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 🔸 2. Canny Edge 적용
    edges = cv2.Canny(gray, 100, 200)

    # 🔸 3. 결과 영상 저장 (isColor=False로 했기 때문에 흑백)
    out.write(edges)

    # 🔸 4. 결과 화면 출력
    cv2.imshow("Processed Frame (Canny)", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🔸 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()
