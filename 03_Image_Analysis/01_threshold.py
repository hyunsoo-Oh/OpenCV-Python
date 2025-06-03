import cv2

# 🔹 이미지를 Grayscale로 불러오기
# - 이진화 처리는 색상이 아닌 밝기 정보를 기준으로 하기 때문에 Grayscale이 필요함
img = cv2.imread("./resources/image.webp", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 1. 단순 임계값 이진화 (Simple Thresholding)
# - 픽셀 값이 127보다 크면 255(흰색), 작으면 0(검정)으로 설정
# - 전체 이미지에 동일한 기준을 적용함
_, binary_simple = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 2. Otsu의 이진화 (Otsu Thresholding)
# - 이미지 히스토그램을 분석해서 **최적의 임계값**을 자동 계산
# - 조명이 일정하지 않은 이미지에서도 단순 임계값보다 정확한 이진화 가능
# - 임계값 자리에 0을 넣고, 플래그에 OTSU를 추가하면 자동 계산됨
_, binary_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 3. 적응형 이진화 (Adaptive Thresholding)
# - 픽셀 주변 영역의 평균 또는 가우시안 가중치를 기준으로 **각 영역별로 다른 임계값**을 적용
# - 국소 영역마다 조도가 다를 경우 (예: 그림자, 강한 명암차) 매우 효과적임
# - 블록 크기(11)와 상수값(2)는 실험적으로 조절 가능
binary_adaptive = cv2.adaptiveThreshold(
    img, 255,                           # 최대값
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,    # 가우시안 가중 평균 방식
    cv2.THRESH_BINARY,                 # 결과 타입 (이진화)
    11,                                # 블록 크기 (11×11 주변 영역)
    2                                  # 평균에서 뺄 상수값 (임계값 조절)
)

# 🔸 결과 이미지 출력
cv2.imshow("Original (Grayscale)", img)
cv2.imshow("Simple Threshold", binary_simple)
cv2.imshow("Otsu Threshold", binary_otsu)
cv2.imshow("Adaptive Threshold", binary_adaptive)

# 🔸 결과 저장
cv2.imwrite("./resources/thresh_simple.webp", binary_simple)
cv2.imwrite("./resources/thresh_otsu.webp", binary_otsu)
cv2.imwrite("./resources/thresh_adaptive.webp", binary_adaptive)

# 🔸 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
