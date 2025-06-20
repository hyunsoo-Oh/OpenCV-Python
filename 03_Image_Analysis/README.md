# 📚 3주차: 에지 검출 & 형태학 처리

영상 내 경계(윤곽선)를 검출하고, 이진화 이미지의 구조를 다듬는 형태학 연산을 학습
Sobel, Laplacian, Canny 같은 고전 에지 검출 필터와 팽창/침식 등의 연산을 실습

## 📁 실습 파일 목록

| 파일명                   | 실습 내용 요약 |
|--------------------------|----------------|
| `01_threshold.py`        | 단순, Otsu, 적응형 이진화 |
| `02_sobel_laplacian.py`  | Sobel 필터 (x, y), Laplacian 필터 |
| `03_canny.py`            | Canny 에지 검출 알고리즘 적용 |
| `04_morphology.py`       | 침식, 팽창, 열림, 닫힘 형태학 연산 |


## 🔍 주요 개념 요약

### ✅ 이진화 (Thresholding)
- **단순 임계값 이진화**: 픽셀값 기준으로 흑/백 결정
- **Otsu 이진화**: 히스토그램 기반 자동 임계값
- **적응형 이진화**: 각 영역별로 임계값 계산 → 조명 변화 대응

### ✅ 에지 검출
- **Sobel 필터**: 1차 미분 기반, 수평/수직 방향 에지 분리 가능
- **Laplacian 필터**: 2차 미분 기반, 방향 구분 없이 전체 경계 감지
- **Canny 알고리즘**: 노이즈 제거 + Non-Max Suppression + 이중 임계값 → 고성능 에지 검출

### ✅ 형태학 연산 (Morphology)
- **침식 (Erosion)**: 객체 축소 → 노이즈 제거
- **팽창 (Dilation)**: 객체 확장 → 끊어진 윤곽 연결
- **열림 (Opening)**: 침식 → 팽창 → 작은 잡음 제거
- **닫힘 (Closing)**: 팽창 → 침식 → 빈 틈 메우기

