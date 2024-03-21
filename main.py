from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

model.train(data='C:/Users/Mehdi/PycharmProjects/pythonProjectKidneyCancer2/data/datasetkc2',
            epochs=2, imgsz=64)
