# To run the script, execute the following commands
# workon cv
# python3 real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
from playsound import playsound
import os
from gtts import gTTS
import pygame
import threading


# def speak(text):#this defines the function SPEAK and creates the command for its use
#this defines the function SPEAK and creates the command for its use
tts = gTTS(text="There is an Object", lang="en")
filename = "voice.mp3"
tts.save(filename)
        # audio_file = os.path.dirname(__file__) + '/voice.mp3'
        # playsound.playsound(audio_file)


def pianoF():
	playsound('voice.mp3')
         #saves the audio file
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required = True,  help = "path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required = True, help = "path to Caffe pre-trained model")
ap.add_argument("-c", "--probability", type = float, default = 0.2, help = "minimum probability to filter weak detections")
args = vars(ap.parse_args())

# initialize the list of class labels MobileNet SSD was trained to detect
# and generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
"dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size = (len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()



class Videotwo(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        frame = vs.read()
        frame = imutils.resize(frame, width=500)

        # grab the frame dimensions and convert it to a blob
        # Binary Large Object = BLOB
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

        # pass the blob through the network and get the detections
        net.setInput(blob)
        detections = net.forward()

        # loop over the detections
        for i in np.arange(0, detections.shape[2]):
            # extract the probability of the prediction
            probability = detections[0, 0, i, 2]

            # filter out weak detections by ensuring that probability is
            # greater than the min probability
            if probability > args["probability"]:
                # extract the index of the class label from the
                # 'detections', then compute the (x, y)-coordinates of
                # the bounding box for the object
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # draw the prediction on the frame
                label = "{}: {:.2f}%".format(CLASSES[idx], probability * 100)
                cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
                t1 = threading.Thread(target=pianoF, args=())
                t1.start()
                t1.join()
            
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()

# # loop over the frames from the video stream
# while True:
# 	# resize the video sstream window at a maximum width of 500 pixels
# 	frame = vs.read()
# 	frame = imutils.resize(frame, width=500)

# 	# grab the frame dimensions and convert it to a blob
# 	# Binary Large Object = BLOB
# 	(h, w) = frame.shape[:2]
# 	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

# 	# pass the blob through the network and get the detections
# 	net.setInput(blob)
# 	detections = net.forward()

# 	# loop over the detections
# 	for i in np.arange(0, detections.shape[2]):
# 		# extract the probability of the prediction
# 		probability = detections[0, 0, i, 2]

# 		# filter out weak detections by ensuring that probability is
# 		# greater than the min probability
# 		if probability > args["probability"]:
# 			# extract the index of the class label from the
# 			# 'detections', then compute the (x, y)-coordinates of
# 			# the bounding box for the object
# 			idx = int(detections[0, 0, i, 1])
# 			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
# 			(startX, startY, endX, endY) = box.astype("int")

# 			# draw the prediction on the frame
# 			label = "{}: {:.2f}%".format(CLASSES[idx], probability * 100)
# 			cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
# 			y = startY - 15 if startY - 15 > 15 else startY + 15
# 			cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
# 			t1 = threading.Thread(target=pianoF, args=())
# 			t1.start()
# 			t1.join()
# 			# speak("The value is" + label)
# 			#check if point is in the first box


# 	# show the output frame
