from ultralytics import YOLO

import numpy as np
from PIL import Image
model = YOLO('yolov8n.pt')
im1 = Image.open("img.png")
sonuc = model.predict(source=im1,save=True)