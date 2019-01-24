# Age recognition
*Authors* Daria Hubernatorova, Piotr Wawrzyniak, Damian Gutowski

The goal of the project was to recognize faces from video camera input and show predicted age. Prediction is based on trained neural network. 
Our method shows similar results as another method on the same dataset.

#### 0. Contents

  - [1. Application](#1-application)
    - [1.1 Modules](#11-modules)
  - [2. Technologies used](#2-technologies-used)
  - [3. Model](#3-model)

## 1. Application
How to use application?
1. Open the site https://agerecognition.mini.pw.edu.pl
2. Allow to use camera when asked.
3. Screenshot of application:

When face is recognized, frame appears with predicted age inside it. If there is no frame try to move closer to camera.

### 1.1. Modules
Application is composed of 2 main modules (Back-end server and Front-end client).
Detailed technical installation and self-hosting instructions can be found here:
  - https://github.com/damian9550/age-recognition-be
  - https://github.com/piotrek29100/age-recognition-client
  
 ## 2. Technologies used
 
  - [Angular CLI](https://github.com/angular/angular-cli)
  - [Python](https://www.python.org/downloads/release/python-360/)
  - [numpy](http://www.numpy.org)
  - [Flask](http://flask.pocoo.org)
  - [Pillow](https://github.com/python-pillow/Pillow/)
  - [Face Recognition](https://github.com/ageitgey/face_recognition)
  - [Keras](https://keras.io)
  - [TensorFlow](https://www.tensorflow.org)

 
## 3. Model
Image from camera is transferred to server. Using face_recognition library face locations are determined. Next, the cropped image of each face is constructed. Image is converted then as float array of shape (1, width, height, 3). ImageDataGenerator from Keras library is used to yield bathches of this input sample to pass it then to prediction function predict_generator. Finally, returned value is decoded by scaling to age range [10, 80].

Model is based on https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/
Dataset comes from IMDB images https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar
