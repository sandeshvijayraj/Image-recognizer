#!/usr/bin/enc python3
from keras import backend as K
abc=[]
def deteft(obj):
	import os
	from imageai.Detection import ObjectDetection
	global abc
	execution_path = os.getcwd()
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , obj))
	for eachObject in detections:
			abc.append(str(eachObject["name"]) + " : " + str(eachObject["percentage_probability"]) )
	K.clear_session()

def objdtc():
	from imageai.Detection import ObjectDetection
	import os
	global abc
	import test as t
	abc=[]
	listimgs=t.listimg()
	print(listimgs)
	for bloo in listimgs:
		print("this is "+bloo)
		deteft(bloo)
	print("here")
	print(abc)
	return abc