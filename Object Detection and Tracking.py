#import libraries

import cv2
import numpy as np



#Load YOLO

net = cv2.dnn.readNet('yolov4.weights', 'yolov4.cfg')  #Replace with yolov3.weights and yolov3.cfg if needed
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
out_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))



#Initialize video capture

cap = cv2.VideoCapture(0)  #Use 0 for webcam, or replace with video file path

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, channels = frame.shape



#Prepare the image for YOLO

    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(out_layers)



#Information about detected objects

    class_ids = []
    confidences = []
    boxes = []



#Use for Loop

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Confidence threshold
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)



#Non-max suppression to avoid multiple boxes for the same object

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f'{label} {confidence:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


#Display the resulting frame
   
   cv2.imshow('Real-Time Object Detection', frame)

#Break loop on 'q' key press

   if cv2.waitKey(1) & 0xFF == ord('q'):
       break


#Release resources

cap.release()
cv2.destroyAllWindows()

