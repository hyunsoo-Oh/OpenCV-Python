# OpenCV Python

## 커리큘럼
- **Getting Started**  
  OpenCV 개발 환경 설정, 이미지 입출력, 웹캠 테스트 등 기본 실습 포함

- **Image Processing**  
  픽셀 연산, 색상 변환, 블러링, 임계값 처리 등 기초 영상 처리 기술 학습

- **Image Analysis**  
  에지 검출(Canny), 형태학 연산(Erosion, Dilation), 윤곽선 추출 등

- **Video Streaming**  
  웹캠 실시간 처리, 동영상 저장 및 재생, 프레임 기반 처리 실습

- **Lane Detection**  
  ROI 설정, Canny + HoughLinesP를 활용한 차선 인식 알고리즘 구현

- **Haar & HOG Detection**  
  Haar Cascade, HOG+SVM을 활용한 얼굴/사람 검출 실습

- **DNN Classification**  
  OpenCV DNN 모듈로 MobileNet 등 사전학습 분류 모델 활용

- **YOLO Detection**  
  YOLOv3 / YOLOv4-tiny 모델을 OpenCV로 로딩하여 객체 검출 실습

- **Object Tracking**  
  MIL, KCF, CSRT 등 객체 추적기 기반 단일/다중 객체 추적 구현

- **Embedded Deploy**  
  Raspberry Pi, Jetson 등의 임베디드 환경에서 영상처리 배포 실습

- **Project Planning**  
  자율주행 보조 시스템과 같은 통합 프로젝트 설계 및 모듈 정의

- **Project Implementation**  
  전체 시스템 구현 및 테스트, 시스템 통합 및 디버깅

- **Presentation & Portfolio**  
  프로젝트 결과 정리, 시연 영상, 발표 슬라이드, README 등 포트폴리오화

## OpenCV Python 설치
### Windows
```
python3 -m venv venv
venv\Scripts\activate
(venv) > pip install opencv-python
```
### Linux
```
python3 -m venv venv
venv/bin/activate
(venv) > pip install opencv-python
```

### Raspberry Pi 4
[1 단계] 전역 패키지 설치
```
sudo apt install -y build-essential cmake git pkg-config \
libjpeg-dev libpng-dev libtiff-dev \
libavcodec-dev libavformat-dev libswscale-dev libv4l-dev v4l-utils \
libgtk-3-dev \
libatlas-base-dev gfortran \
python3-dev python3-numpy \
libqtgui4 libqt4-test libxvidcore-dev libx264-dev \
libopenblas-dev liblapack-dev libhdf5-dev
```
[2 단계] OpenCV 소스코드 다운로드
```
mkdir ~/opencv_build && cd ~/opencv_build

# OpenCV 본체
git clone https://github.com/opencv/opencv.git
# OpenCV의 extra 모듈 (선택적이지만 추천)
git clone https://github.com/opencv/opencv_contrib.git

# 안정 버전으로 체크아웃 (예: 4.8.0)
cd opencv
git checkout 4.8.0
cd ../opencv_contrib
git checkout 4.8.0
```
[3 단계] 빌드 디렉토리 생성 및 설정
```
cd ~/opencv_build
mkdir build && cd build
```
[4 단계] CMake 구성
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
      -D ENABLE_NEON=ON \
      -D ENABLE_VFPV3=ON \
      -D BUILD_TESTS=OFF \
      -D BUILD_EXAMPLES=OFF \
      -D BUILD_opencv_python3=ON \
      -D OPENCV_ENABLE_NONFREE=ON \
      -D WITH_V4L=ON \
      -D WITH_QT=ON \
      -D WITH_OPENGL=ON \
      -D BUILD_NEW_PYTHON_SUPPORT=ON \
      -D PYTHON3_EXECUTABLE=$(which python3) \
      -D PYTHON3_INCLUDE_DIR=$(python3 -c "from sysconfig import get_paths as gp; print(gp()['include'])") \
      -D PYTHON3_PACKAGES_PATH=$(python3 -c "from sysconfig import get_paths as gp; print(gp()['purelib'])") \
      ../opencv
```
[4 단계] 컴파일 및 설치

```
make -j$(nproc)
sudo make install
sudo ldconfig
```
[5 단계] 설치 확인
```
import cv2
print(cv2.__version__)
```
