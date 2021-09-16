import os
# to supress the warning messages in command line
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import tensorflow as tf
# to supress the warning messages in command line
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import cv2
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np


#initializing the models and camera
name="User"
labels = ['Kunal', 'Ritik', 'Abhijeet']
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('facecapture\\keras_model.h5')
face_cascade = cv2.CascadeClassifier("facecapture\\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

print("Stating...")

"""
The function tech takes a gray scale image as an input and perform facial reccognition
using the model trained on Google's Teachable Machine.
"""

def teac(img):
    image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    pilImage=Image.fromarray(image)
    image = ImageOps.fit(pilImage, (224,224), Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    i=np.argmax(prediction[0], axis=0)
    return labels[i]

"""
The function capAndRec use openCv to capture frames from the camera
and then convert those frames into gray scale and pass them to teach function to perform facial rec
and return the name of the persone recognised from the image input.
"""

def capAndRec():
    frames=0
    while frames<10:
        _, img = cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, 1.1, 4)
        name=teac(img)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,name,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        frames+=1
    cap.release()
    return name

if __name__ == "__main__":
    print(capAndRec())



