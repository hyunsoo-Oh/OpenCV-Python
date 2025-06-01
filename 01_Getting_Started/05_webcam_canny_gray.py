import cv2  # OpenCV 라이브러리 임포트

# 🎥 기본 웹캠(장치 0) 열기
cap = cv2.VideoCapture(0)

# 카메라가 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("❌ 카메라를 열 수 없습니다.")
    exit()

while True:
    # 📸 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        print("❌ 프레임 읽기 실패")
        break

    # 🎨 컬러 → 그레이스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 🔍 Canny 에지 검출 (임계값 조정 가능)
    edges = cv2.Canny(gray, 100, 200)

    # 🪞 세 개의 영상 출력
    cv2.imshow("Original", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Canny Edge", edges)

    # ⏱️ 'q' 키 입력 시 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🎬 리소스 해제
cap.release()
cv2.destroyAllWindows()
