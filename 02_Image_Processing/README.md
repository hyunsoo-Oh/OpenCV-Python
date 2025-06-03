# 📚 2주차: 이미지 처리 기초

OpenCV Python을 이용해 기본적인 이미지 처리 기법들을 실습  
컬러 공간 변환, 리사이징, 자르기, 채널 분리 및 병합, 블러링 등의 기초 기술 학습

---

## 📁 실습 파일 목록

| 파일명               | 실습 내용 요약 |
|---------------------|----------------|
| `01_convert.py`     | BGR 이미지를 Grayscale 및 HSV 컬러 공간으로 변환 |
| `02_resize.py`      | 절대 크기 및 비율 기반 이미지 리사이징 실습 |
| `03_crop.py`        | 이미지에서 관심 영역(ROI)을 좌표로 잘라내기 |
| `04_split_merge.py` | 이미지의 B, G, R 채널 분리 및 병합 |
| `05_blur.py`        | 평균 블러 및 가우시안 블러 적용 및 비교 |


## 🔍 주요 개념 요약

### ✅ 컬러 공간 변환
- `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`
- `cv2.cvtColor(img, cv2.COLOR_BGR2HSV)`
- 전처리, 객체 탐지, 피부색 필터링 등에 활용

### ✅ 이미지 리사이징
- 절대 크기: `cv2.resize(img, (width, height))`
- 비율 기반: `cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)`
- 보간법: `INTER_LINEAR`, `INTER_AREA`, `INTER_CUBIC` 등

### ✅ 자르기 (Crop)
- NumPy 슬라이싱 사용: `img[y:y+h, x:x+w]`
- 관심 영역만 추출하여 별도 처리 가능

### ✅ 채널 분리 및 병합
- `cv2.split(img)` → B, G, R 채널 추출
- `cv2.merge([b, g, r])` → 채널 병합
- 단일 채널 시각화는 나머지 채널을 0으로 병합해 표현

### ✅ 블러링 (Blur)
- 평균 블러: `cv2.blur(img, (5, 5))`
- 가우시안 블러: `cv2.GaussianBlur(img, (5, 5), 0)`
- 노이즈 제거, 경계 부드럽게 처리 등 용도
