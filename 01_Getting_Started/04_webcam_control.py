import cv2  # OpenCV 모듈 임포트

# 🎥 0번 카메라 장치 열기 (내장 웹캠 or USB 카메라)
cap = cv2.VideoCapture(0)

# 카메라 열기 실패 시 오류 처리
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    # 📸 현재 프레임 읽기 (ret: 성공 여부, frame: 이미지)
    ret, frame = cap.read()
    
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 🪞 영상 출력 (윈도우 이름, 이미지 데이터)
    cv2.imshow("Webcam Live", frame)

    # ⏱️ 1ms 대기 후 키 입력 확인 (q 키 누르면 종료)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🎬 사용한 카메라 장치 해제
cap.release()

# 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
