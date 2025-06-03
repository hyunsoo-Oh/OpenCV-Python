# 📚 5주차: 차선 인식 및 마스크 처리

이번 주차에서는 도로 위 **차선을 추출하기 위한 전처리 기술**들을 학습합니다.  
색상 기반 필터링, 관심 영역(ROI) 지정, 에지 검출(Canny), Hough Transform을 조합해  
**차선을 검출하고 직선으로 시각화하는 통합 파이프라인**을 완성합니다.

## 📁 실습 파일 목록

| 파일명                  | 실습 내용 요약 |
|-------------------------|----------------|
| `01_color_mask.py`      | HSV 색공간에서 흰색/노란색 차선 마스킹 |
| `02_roi_mask.py`        | ROI 설정으로 하단 도로 영역만 추출 |
| `03_lane_detection.py`  | Canny + Hough Transform으로 차선 검출 |


## 🔍 주요 개념 요약

### ✅ 1. 색상 기반 마스킹 (`cv2.inRange`)
- **HSV 색공간**을 사용해 흰색, 노란색 계열 필터링
- `bitwise_or()`로 두 마스크 결합

```python
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 25, 255])
mask_white = cv2.inRange(hsv, lower_white, upper_white)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

mask = cv2.bitwise_or(mask_white, mask_yellow)
```
### ✅ 2. 관심 영역 (ROI: Region of Interest)
도로 하단 또는 사다리꼴 영역만 선택하여 불필요한 배경 제거
```python
roi = np.zeros_like(mask)
polygon = np.array([[
    (width * 0.1, height),
    (width * 0.45, height * 0.6),
    (width * 0.55, height * 0.6),
    (width * 0.9, height)
]], dtype=np.int32)

cv2.fillPoly(roi, polygon, 255)
masked_roi = cv2.bitwise_and(mask, roi)
```

### ✅ 3. 에지 검출 (cv2.Canny)
ROI 마스크를 GaussianBlur 처리 후 Canny 적용
```python
blur = cv2.GaussianBlur(masked_roi, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
```

### ✅ 4. Hough Line Transform (cv2.HoughLinesP)
에지 위에서 직선을 검출하고 선으로 시각화
```python
lines = cv2.HoughLinesP(
    edges, 1, np.pi / 180,
    threshold=80,
    minLineLength=100,
    maxLineGap=40
)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
```