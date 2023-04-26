from ultralytics import YOLO
import cv2


model_path = '/media/veracrypt2/computer_vision/47_pose_detection_yolov8/code/runs/pose/train9/weights/last.pt'

image_path = './samples/wolf.jpg'
img = cv2.imread(image_path)

model = YOLO(model_path)

results = model(image_path)[0]

for result in results:
    for keypoint_indx, keypoint in enumerate(result.keypoints.tolist()):
        cv2.putText(img, str(keypoint_indx), (int(keypoint[0]), int(keypoint[1])),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
