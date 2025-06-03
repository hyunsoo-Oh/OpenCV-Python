# 📌 09주차: 객체 추적 (Object Tracking)

## 🧠 학습 목표
- OpenCV에서 다양한 추적기(Tracker)를 활용하여 **단일/다중 객체 추적** 구현
- 여러 추적기의 성능을 **속도, 정확도, 안정성** 기준으로 비교
- 실제 영상에서 추적 성능을 눈으로 확인하고 **적합한 추적기 선택 기준** 이해


## 🗂 실습 파일 목록

| 파일명 | 실습 내용 요약 |
|--------|----------------|
| `01_single_object_tracking.py` | 단일 객체를 **CSRT 추적기**로 추적. `cv2.TrackerCSRT_create()` 사용 |
| `02_multi_object_tracking.py` | 여러 객체를 동시에 추적. `cv2.MultiTracker_create()` 및 `selectROIs()` 사용 |
| `03_compare_tracker.py` | **CSRT, KCF, MIL, MOSSE, BOOSTING** 추적기를 한 화면에 비교 시각화 |


## 🧰 사용된 주요 함수 및 클래스

| 함수 / 클래스 | 설명 |
|---------------|------|
| `cv2.selectROI()` / `selectROIs()` | 마우스로 객체를 직접 선택하여 추적 대상 설정 |
| `cv2.TrackerCSRT_create()` 등 | 다양한 추적기 생성 함수 (legacy 포함) |
| `cv2.MultiTracker_create()` | 다중 객체 추적을 위한 추적기 묶음 생성 |
| `tracker.init(frame, bbox)` | 추적기 초기화: 대상 객체 좌표 설정 |
| `tracker.update(frame)` | 프레임별 추적 결과 업데이트 |
| `cv2.hconcat()`, `cv2.vconcat()` | 결과 영상 여러 개를 한 화면에 결합하여 시각화 |


## 📊 추적기 비교 요약

| 추적기 | 특징 |
|--------|------|
| **CSRT** | 정확도 매우 높음, 속도는 느림 |
| **KCF** | 속도와 정확도 균형 |
| **MIL** | 가벼우나 추적 정확도 낮음 |
| **MOSSE** | 매우 빠름, 단순한 환경에 적합 |
| **BOOSTING** | OpenCV의 초기 추적기, 정확도 낮음 |


## 💡 실습 팁

- **객체가 가려지거나 사라지면** 추적기 대부분은 추적 실패
- 객체가 다시 나타나도 **재식별 불가**
- 이런 한계를 극복하려면 다음 주차의 **YOLO + SORT/DeepSORT** 실습으로 확장 가능
