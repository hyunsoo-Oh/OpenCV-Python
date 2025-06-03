import cv2

# [1] 영상 경로 설정 (드론 영상)
video_path = "./09_Object_Tracking/data/videos/sample.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ 비디오를 열 수 없습니다.")
    exit()

# [2] 첫 프레임에서 객체 선택
ret, frame = cap.read()
if not ret:
    print("❌ 첫 프레임을 읽을 수 없습니다.")
    exit()

# 객체 선택 (마우스로 드래그)
bbox = cv2.selectROI("Select Object to Track", frame, fromCenter=False)
cv2.destroyWindow("Select Object to Track")

# [3] 추적기 초기화 (CSRT: 정확도 높음)
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

# [4] 프레임 반복
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 객체 추적
    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

    # 결과 출력
    cv2.imshow("Single Object Tracking", frame)
    key = cv2.waitKey(10)
    if key == 7:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
