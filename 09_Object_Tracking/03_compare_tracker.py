import cv2

# [1] 사용할 추적기 생성 함수들을 딕셔너리로 정의
tracker_types = {
    "CSRT": cv2.legacy.TrackerCSRT_create,
    "KCF": cv2.legacy.TrackerKCF_create,
    "MIL": cv2.legacy.TrackerMIL_create,
    "MOSSE": cv2.legacy.TrackerMOSSE_create,
    "BOOSTING": cv2.legacy.TrackerBoosting_create
}

# [2] 영상 열기
video_path = "./09_Object_Tracking/data/videos/sample2.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ 비디오를 열 수 없습니다.")
    exit()

# [3] 첫 프레임 읽기
ret, frame = cap.read()
if not ret:
    print("❌ 첫 프레임을 읽을 수 없습니다.")
    exit()

# [4] 객체 선택 (ROI) – 사용자가 하나의 객체를 지정
bbox = cv2.selectROI("Select ROI for Comparison", frame, fromCenter=False)
cv2.destroyWindow("Select ROI for Comparison")

# [5] 각 추적기 초기화
trackers = {}
init_frames = {}

for name, creator in tracker_types.items():
    tracker = creator()
    # 원본 프레임 복사 (각 추적기가 개별 프레임에서 동작하도록)
    init_frame = frame.copy()
    tracker.init(init_frame, bbox)
    trackers[name] = tracker
    init_frames[name] = init_frame

# [6] 프레임 반복
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 결과 저장할 리스트
    results = []

    # [7] 각 추적기 별로 개별 프레임 복사 → update 후 사각형 표시
    for name, tracker in trackers.items():
        frame_copy = frame.copy()
        success, box = tracker.update(frame_copy)

        if success:
            x, y, w, h = map(int, box)
            cv2.rectangle(frame_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame_copy, f"{name}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            cv2.putText(frame_copy, f"{name} - Lost", (20, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        results.append(frame_copy)

    # [8] 추적기 화면을 2x3 타일로 붙이기
    row1 = cv2.hconcat(results[:3])

    if len(results) > 3:
        row2 = cv2.hconcat(results[3:])
        # 두 row의 너비가 같도록 resize
        if row1.shape[1] != row2.shape[1]:
            row2 = cv2.resize(row2, (row1.shape[1], row2.shape[0]))
        final = cv2.vconcat([row1, row2])
    else:
        final = row1


    # [9] 화면 출력
    cv2.imshow("Tracker Comparison", final)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
