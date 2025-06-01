import cv2  # OpenCV 모듈 임포트

# 🎞️ 저장된 동영상 파일 열기
cap = cv2.VideoCapture("./resources/output.avi")

# 파일 열기 실패 시 종료
if not cap.isOpened():
    print("❌ 영상 파일을 열 수 없습니다.")
    exit()

# 🎬 동영상 재생
while True:
    ret, frame = cap.read()
    if not ret:
        print("🔚 영상 재생 완료 또는 프레임 읽기 실패")
        break

    # 🪞 현재 프레임 화면에 출력
    cv2.imshow("Playback", frame)

    # ⏱️ 30ms마다 다음 프레임 (실제 FPS에 따라 조절 가능)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# 🔚 리소스 정리
cap.release()
cv2.destroyAllWindows()
