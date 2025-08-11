import torch
from PIL import Image

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_objects(img_path):
    img = Image.open(img_path)
    results = model(img)
    detections = results.pandas().xyxy[0]
    athletes = detections[detections['name'] == 'person']
    return {
        "num_athletes": len(athletes),
        "bbox": athletes[['xmin', 'ymin', 'xmax', 'ymax']].values.tolist()
    }
