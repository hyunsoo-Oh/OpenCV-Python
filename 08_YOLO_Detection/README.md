# 🧠 YOLOv5s ONNX Runtime 객체 검출 실습

YOLOv5s 모델을 ONNX 포맷으로 불러와 `onnxruntime`을 통해 추론하며, OpenCV로 결과를 시각화

오검출(Over-detection) 문제를 해결하기 위한 필터링 및 시각화 개선을 적용한 버전


## ✅ 모델 정보

| 항목    | 값                     |
| ----- | --------------------- |
| 모델    | YOLOv5s               |
| 형식    | ONNX (.onnx)          |
| 입력 크기 | 640 × 640 RGB         |
| 클래스 수 | 80 (COCO dataset 기준)  |
| 엔진    | ONNX Runtime + OpenCV |

## 🧪 주요 개선 사항

| 항목                   | 값                                 |
| -------------------- | --------------------------------- |
| Confidence Threshold | `0.85`                            |
| NMS Threshold        | `0.3`                             |
| 허용 클래스 필터링           | 예시: `{'person', 'chair'}`         |
| 최대 박스 수 제한           | `50개`                             |
| 텍스트 시각화 폰트 크기        | `0.4`                             |
| 선 두께 / 라인 부드럽게       | `thickness=1`, `lineType=LINE_AA` |
| 이미지 확대               | `cv2.resize()`로 1.5\~2.0배 확대      |
