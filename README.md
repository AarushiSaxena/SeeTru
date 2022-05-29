
# Project Title

SEETRU : Creating Vision without Sight! 

# Project Description

This project aims to classify the emotion on a person's face into one of seven categories, using deep convolutional neural networks. People with visual impairments face difficulties during social interactions. In order to assist them, designed system to identify the expressionS of the confronting person and hence enable a better communication. In this system the blind person uses camera assistance for image acquisition of the person who is interacting with them and by using an audio device the facial emotion is detected and conveyed. 

# Dependencies

• Python 3, OpenCV, Tensorflow, Playsound

• To install the required packages, run `pip install -r requirements.txt`

# Data Preparation and Usage

• In case you are looking to experiment with new datasets, you may have to deal with data in the csv format. I have provided the code I wrote for data preprocessing in the dataset_prepare.py file which can be used for reference.

• Initialize the repository:

cd Emotion-detection

• If you want to train this model, use:

cd src
                                                                                                                                                                                                                                                                                                                                                                                                                                                       
python emotions.py --mode train

• If you want to view the predictions without training again, you can download the pre-trained model from here and then run:

cd src   
python emotions.py --mode display

# Additonal Features

• If you want to use the object-detection model, run:

python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

• If you want to use the denomination-determinor model, run:

python main2.py


# Implementation

• Algorithm for Emotion Detection

1. The haar cascade method is used to detect faces in each frame of the webcam feed.
2. The region of image containing the face is resized to 48x48 and is passed as input to the CNN. 
3. The network outputs a list of softmax scores for the seven classes of emotions.
4. The emotion with maximum score is displayed on the screen.

• Algorithm for Denomination Determinor:

1. The currency note should occupy at least 1/6 of the whole image
2. The currency note should be displayed from different angles in the image
3. The currency note should be present in various locations in the image (top left corner, middle, bottom right corner, etc.)
4. There should be some foreground objects covering part of the currency (no more than 40% though)
5. The background should be as diversified as possible


• Algorithm for Object Detection

1. Looping through our detections, first we extract the confidence value.
2. If the confidence is above our minimum threshold, we extract the class label index and compute the bounding box coordinates around the detected object.
3. Then, we extract the (x, y)-coordinates of the box which we will will use for drawing a rectangle and displaying the label text.
4. We build a text label containing the CLASS name and the confidence
5. We also draw a colored rectangle around the object using our class color and previously extracted (x, y)-coordinates.





## License

[MIT](https://choosealicense.com/licenses/mit/)

