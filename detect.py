from imageai.Detection import ObjectDetection
import os
from PIL import Image
import numpy as np
import cv2
import io

def get_image_from_file(filename):
	with open(filename, 'rb') as imgfile:
		return imgfile.read()

image_bytes = get_image_from_file('./work.jpg')
# source = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
source = np.asarray(Image.open(io.BytesIO(image_bytes)), dtype='float64')

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
# detector.setModelPath( os.path.join(execution_path , "yolo-tiny.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=source, input_type="array")

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )


