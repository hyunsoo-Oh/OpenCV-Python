import cv2

# [1] 카메라 열기 (0 = 기본 웹캠)
cap = cv2.VideoCapture(0)

# [2] 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("❌ 카메라를 열 수 없습니다.")
    exit()

# [3] 프레임 반복
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 프레임을 읽을 수 없습니다.")
        break

    # [4] 영상 출력
    cv2.imshow("Live Camera", frame)

    # [5] 키 입력 대기 (ESC 또는 q 키 누르면 종료)
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

# [6] 자원 해제
cap.release()
cv2.destroyAllWindows()
