## 📘 1주차 요약: 01_Getting_Started
### 🎯 학습 목표
- OpenCV 개발 환경 설정 (pip/venv)

- 이미지 및 동영상 파일 입출력

- 웹캠 영상 처리 실습

- 영상 저장 및 재생

## 📁 폴더 구성
```
01_Getting_Started/
├── 01_cv2test.py              # OpenCV 설치 확인 및 간단 테스트
├── 02_using_img.py            # 이미지 불러오기, 출력, 저장
├── 03_webcam_streaming.py     # 웹캠 실시간 영상 출력
├── 04_webcam_control.py       # 웹캠 + 'q' 키 종료 제어
├── 05_webcam_canny_gray.py    # 실시간 영상 + 그레이스케일 + 에지 검출
├── 06_webcam_recording.py     # 웹캠 영상 저장 (.avi)
├── 07_video_playback.py       # 저장된 영상 파일 재생
```

## 📌 주요 함수 정리
| 함수                           | 설명                      |
| ---------------------------- | ----------------------- |
| `cv2.imread(path)`           | 이미지 파일 읽기               |
| `cv2.imshow(title, img)`     | 이미지/프레임 출력              |
| `cv2.imwrite(filename, img)` | 이미지 저장                  |
| `cv2.VideoCapture(0)`        | 웹캠 열기                   |
| `cap.read()`                 | 카메라/영상의 프레임 읽기          |
| `cv2.VideoWriter()`          | 영상 저장 객체 생성             |
| `out.write(frame)`           | 프레임 단위 저장               |
| `cv2.Canny()`                | 에지 검출                   |
| `cv2.cvtColor(img, flag)`    | 색상 변환 (e.g. BGR → GRAY) |
