# 📚 4주차: 영상 입출력 및 동영상 처리

이번 주차에서는 OpenCV로 실시간 영상 스트리밍을 처리하는 기초를 학습
웹캠 또는 동영상 파일로부터 프레임을 읽고, 저장하며, 실시간 처리 필터를 적용하는 방법

## 📁 실습 파일 목록

| 파일명                    | 실습 내용 요약 |
|---------------------------|----------------|
| `01_video_read.py`        | 웹캠 또는 동영상 파일에서 프레임 읽고 출력 |
| `02_video_save.py`        | 웹캠 프레임을 실시간으로 저장 (`.avi` 동영상 생성) |
| `03_video_processing.py`  | 실시간 프레임 처리 (예: Canny Edge) 후 저장 및 출력 |

## 🔍 주요 개념 요약

### ✅ 영상 입력 (`cv2.VideoCapture`)
- `cv2.VideoCapture(0)` → 기본 카메라
- `cv2.VideoCapture("video.mp4")` → 영상 파일
- `.read()`로 프레임 단위 읽기  
- `.set(CAP_PROP_*)`로 해상도, FPS 등 설정 가능

### ✅ 영상 출력 (`cv2.imshow`)
- 실시간 프레임을 화면에 출력
- `waitKey(ms)`로 프레임 전환 속도 제어
- `'q'` 키로 루프 종료 처리

### ✅ 영상 저장 (`cv2.VideoWriter`)
- `VideoWriter_fourcc(*'XVID')` → 코덱 설정
- 저장 FPS, 프레임 크기, 색상 여부 설정
- `.write(frame)`으로 프레임 저장

### ✅ 실시간 처리 예시
- `cv2.Canny()` → 경계선 검출
- `cv2.cvtColor(..., COLOR_BGR2GRAY)` → 흑백 전환
- `cv2.GaussianBlur`, `threshold`, `morphologyEx` 등도 활용 가능
