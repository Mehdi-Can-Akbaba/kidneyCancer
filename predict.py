from ultralytics import YOLO

import numpy as np
from PIL import Image

model = YOLO('./runs/classify//ep2/weights/last.pt')  # load a custom model


#im1= Image.open("./data/datasetkc/train/Tumor/Tumor- (831).jpg")
#sonuc2 = model.predict(source=im1, save=True)  # predict on an image


sonuc = model('./data/datasetkc2/train/Stone/Stone- (1359).jpg',save=True)  # predict

names_dict = sonuc[0].names

probs = sonuc[0].probs.data.tolist()

print(names_dict)

print(probs)

print("Bu görselin sınıfı:",names_dict[np.argmax(probs)])
