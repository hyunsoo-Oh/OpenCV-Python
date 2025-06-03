import cv2

# [1] 영상 파일 경로 지정 및 VideoCapture 객체 생성
video_path = "./09_Object_Tracking/data/videos/sample2.mp4"
cap = cv2.VideoCapture(video_path)

# [2] 비디오 파일이 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("❌ 비디오를 열 수 없습니다.")
    exit()

# [3] 첫 번째 프레임 읽기 (객체 선택을 위해 필요)
ret, frame = cap.read()
if not ret:
    print("❌ 첫 프레임을 읽을 수 없습니다.")
    exit()

# [4] 여러 객체 선택 (ROI: Region of Interest)
# 마우스로 추적할 영역을 직접 지정할 수 있으며, 여러 개 선택 가능
bboxes = cv2.selectROIs("Select Multiple Objects", frame, fromCenter=False)
# 선택 창 종료
cv2.destroyWindow("Select Multiple Objects")

# [5] MultiTracker 객체 생성 (여러 개의 추적기를 동시에 관리)
multi_tracker = cv2.legacy.MultiTracker_create()

# [6] 선택한 각 ROI에 대해 CSRT 기반 추적기 생성 및 MultiTracker에 추가
for bbox in bboxes:
    # CSRT 추적기 생성 (정확도가 높고 안정적임)
    tracker = cv2.legacy.TrackerCSRT_create()
    # MultiTracker에 (추적기, 초기 프레임, ROI) 등록
    multi_tracker.add(tracker, frame, bbox)

# [7] 프레임 반복 처리 (비디오가 끝날 때까지)
while True:
    ret, frame = cap.read()
    if not ret:
        break  # 비디오가 끝나면 종료

    # [8] 모든 추적기에 대해 현재 프레임에서 객체 위치 갱신
    success, boxes = multi_tracker.update(frame)

    # [9] 갱신된 각 추적 결과(좌표)에 대해 사각형과 텍스트 출력
    for i, new_box in enumerate(boxes):
        x, y, w, h = map(int, new_box)  # float → int로 변환
        # 추적된 객체 위치에 초록색 사각형 표시
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 객체 번호를 화면에 출력
        cv2.putText(frame, f"Object {i+1}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # [10] 결과 프레임 출력
    cv2.imshow("Multi Object Tracking", frame)

    # [11] 키 입력 대기 (ESC 입력 시 종료)
    if cv2.waitKey(10) & 0xFF == 7:
        break

# [12] 자원 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
