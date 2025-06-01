import cv2  # OpenCV 모듈 임포트

# 🎥 웹캠 열기 (0번 장치)
cap = cv2.VideoCapture(0)

# 웹캠이 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("❌ 카메라를 열 수 없습니다.")
    exit()

# 🛠️ 프레임 정보 (너비, 높이, FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # 보통 640
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 보통 480
fps = 20.0  # 프레임 속도

# 💾 영상 저장 설정 (파일명, 코덱, FPS, 프레임 크기)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 'XVID' 코덱: .avi 저장용
out = cv2.VideoWriter('./resources/output.avi', fourcc, fps, (frame_width, frame_height))

print("🎬 저장 시작... 'q' 키로 종료")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 프레임 읽기 실패")
        break

    # 📝 프레임 저장
    out.write(frame)

    # 🪞 화면에도 출력
    cv2.imshow("Recording...", frame)

    # ⏱️ 'q' 입력 시 저장 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🔚 모든 리소스 정리
cap.release()
out.release()
cv2.destroyAllWindows()
print("✅ 영상 저장 완료: output.avi")
