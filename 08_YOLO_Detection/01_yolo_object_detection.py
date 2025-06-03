import cv2
import numpy as np
import onnxruntime as ort

# [1] 모델 및 테스트 이미지 경로 설정
model_path = './08_YOLO_Detection/models/yolov5s.onnx'
image_path = './08_YOLO_Detection/data/test_images/office.jpeg'  # COCO 클래스가 포함된 이미지 사용

# [2] COCO 클래스 이름 정의 (YOLOv5는 80개의 클래스를 학습)
class_names = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
    "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
    "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
    "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
    "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
    "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]

# [3] 이미지 로드 및 전처리
img = cv2.imread(image_path)
if img is None:
    print("❌ 이미지 로드 실패! 경로를 확인하세요.")
    exit()

# 원본 이미지 크기 저장 (추후 박스 복원 시 필요)
orig_h, orig_w = img.shape[:2]

# YOLOv5는 640x640 RGB 입력을 받으므로 리사이즈 및 전처리
input_image = cv2.resize(img, (640, 640))
blob = cv2.dnn.blobFromImage(input_image, scalefactor=1/255.0,
                             size=(640, 640), swapRB=True, crop=False)
input_tensor = blob.astype(np.float32)

# [4] ONNX Runtime으로 모델 로드 및 추론 수행
session = ort.InferenceSession(model_path)
input_name = session.get_inputs()[0].name
outputs = session.run(None, {input_name: input_tensor})[0]  # shape: (1, 25200, 85)

# [5] 결과 후처리
boxes, confidences, class_ids = [], [], []
output = outputs.squeeze(0)  # shape: (25200, 85)

# confidence threshold 설정 (과다 검출 방지용)
CONFIDENCE_THRESHOLD = 0.8
NMS_THRESHOLD = 0.3

# (선택) 특정 클래스만 허용하고 싶다면 여기에 추가
# allowed_classes = {'person', 'cell phone', 'laptop'}  # 예시
allowed_classes = ['person']  # 모든 클래스 허용

for det in output:
    scores = det[5:]
    class_id = np.argmax(scores)
    confidence = scores[class_id]

    # 기준 이상의 신뢰도를 가진 경우만 필터링
    if confidence > CONFIDENCE_THRESHOLD:
        if allowed_classes and class_names[class_id] not in allowed_classes:
            continue

        cx, cy, w, h = det[0:4]
        # 원본 이미지 기준 좌표로 환산
        x = int((cx - w / 2) * orig_w / 640)
        y = int((cy - h / 2) * orig_h / 640)
        w = int(w * orig_w / 640)
        h = int(h * orig_h / 640)

        boxes.append([x, y, w, h])
        confidences.append(float(confidence))
        class_ids.append(class_id)

# [6] 비최대 억제 (NMS)로 겹치는 박스 제거
indices = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)

# [7] 결과 이미지에 경계 박스와 라벨 출력
for i in indices.flatten():
    x, y, w_box, h_box = boxes[i]
    label = f"{class_names[class_ids[i]]}: {confidences[i]*100:.1f}%"

    # 경계 박스 그리기
    cv2.rectangle(img, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)

    # 라벨 텍스트 출력
    cv2.putText(
        img, label, (x, max(y - 10, 0)),   # y가 음수가 되지 않도록
        cv2.FONT_HERSHEY_SIMPLEX, 
        0.4,              # Font 크기 ↓
        (0, 0, 255),      # 색깔 유지
        1,                # 얇게
        lineType=cv2.LINE_AA  # 부드럽게
    )

# [8] 결과 이미지 출력
cv2.namedWindow("YOLOv5 ONNX Runtime", cv2.WINDOW_NORMAL)  # 창 크기 조절 가능하게 설정
cv2.resizeWindow("YOLOv5 ONNX Runtime", 1280, 960)          # 원하는 창 크기 (가로 × 세로)
cv2.imshow("YOLOv5 ONNX Runtime", img)
cv2.imshow("YOLOv5 ONNX Runtime - Filtered", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
