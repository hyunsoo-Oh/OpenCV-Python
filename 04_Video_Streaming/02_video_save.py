import cv2

# 🔹 카메라 초기화
cap = cv2.VideoCapture(0)

# 권장 해상도 및 FPS 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# 실제 적용된 정보 확인
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)
print(f"해상도: {width} x {height}, FPS: {fps}")

# 🔸 VideoWriter 초기화
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정 (XVID, MJPG, MP4V 등 가능)
out = cv2.VideoWriter('./resources/output_video.avi', fourcc, fps, (width, height))

# 🔸 프레임 저장 루프
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 저장
    out.write(frame)

    # 동시에 출력
    cv2.imshow("Recording...", frame)

    # 'q' 키 입력 시 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🔸 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()
