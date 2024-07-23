import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

model = YOLO("model/weights/last.pt")
threshold = 0.5
while True:
    # img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model.predict(frame)
    # count_text = 0
    for result in results:
        for res in result.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = res
            print(score)
            if score > threshold:
                # count_text += 1
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, result.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow("object detaction", frame)
    ret, frame = cap.read()
    cv2.waitKey(1)
