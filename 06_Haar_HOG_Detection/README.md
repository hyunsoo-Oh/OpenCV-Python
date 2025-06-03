# 🧠 6주차: 고전 객체 검출 (Haar, HOG)

**기본 객체 검출 알고리즘**인 Haar Cascade와 HOG + SVM을 활용하여 얼굴 및 사람을 검출하는 실습


## 📚 학습 목표

- Haar 특징 기반 Cascade 분류기를 이해하고, 얼굴 검출에 적용할 수 있다.
- HOG(Histogram of Oriented Gradients) + SVM 조합을 통해 사람(보행자) 검출을 수행할 수 있다.
- 고전 방식 객체 검출의 한계와 DNN 기반 검출과의 차이를 파악할 수 있다.

## 🧪 실습 목록

| 실습 파일명 | 내용 요약 |
|-------------|-----------|
| `01_face_detection_haar.py` | Haar Cascade를 이용하여 얼굴을 검출하고, 그 결과를 이미지에 시각화 |
| `02_people_detection_hog.py` | HOG + SVM 기반 보행자 검출기(HOGDescriptor)를 활용하여 이미지 내 사람 검출 |

## 🔍 실습 요약

### ✅ 01_face_detection_haar.py

- `cv2.CascadeClassifier()`를 이용해 Haar cascade XML 모델 로드
- Grayscale 변환 후 `detectMultiScale()`로 얼굴 검출
- 측면 얼굴, 얼굴 일부 가림 등에는 취약
- `minNeighbors`, `minSize`, `scaleFactor`를 조정하여 오탐/미탐을 줄일 수 있음

### ✅ 02_people_detection_hog.py

- `cv2.HOGDescriptor()`를 이용해 사람 검출
- 사전 학습된 SVM 모델(`getDefaultPeopleDetector()`) 사용
- 작은 사람, 겹친 사람에 대한 검출 정확도는 낮음
- `winStride`, `padding`, `scale` 조정을 통해 정밀도/속도 균형 조절

## 🧠 보충 설명

| 알고리즘 | 장점 | 단점 |
|----------|------|------|
| Haar Cascade | 빠름, 간단함 | 정면 얼굴 외에는 부정확, 오탐 많음 |
| HOG + SVM | 고전적인 사람 검출에 유용 | 작은 객체나 복잡한 장면에는 부정확 |

---

## 📌 실습용 이미지 경로

- 모든 실습은 **`./resources/image.webp`** 파일을 기준으로 진행함
- 적절한 이미지가 없을 경우 OpenCV 샘플 이미지나 직접 준비한 이미지 사용 가능
