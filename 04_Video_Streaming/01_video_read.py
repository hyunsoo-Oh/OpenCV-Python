import cv2

# 🔹 1. 영상 소스 선택
# 0 → 기본 웹캠 사용 (노트북 or USB 캠)
# "sample.mp4" → 파일 경로 사용 가능
cap = cv2.VideoCapture(0)  # 또는 cv2.VideoCapture("./resources/sample.mp4")

# 해상도 조절 (권장)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fps = cap.get(cv2.CAP_PROP_FPS)
print(f"현재 FPS: {fps}")

cap.set(cv2.CAP_PROP_FPS, 30)  # 예: 30fps로 설정

# 🔸 캡처가 열렸는지 확인
if not cap.isOpened():
    print("🎥 영상을 열 수 없습니다.")
    exit()

# 🔸 2. 프레임 읽기 루프
while True:
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:
        print("📭 더 이상 읽을 프레임이 없습니다.")
        break

    # 🔹 프레임 출력
    cv2.imshow("Video Frame", frame)

    # 🔸 3. 키보드 입력으로 종료 ('q' 입력 시 종료)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🔸 4. 자원 해제 및 종료
cap.release()
cv2.destroyAllWindows()
