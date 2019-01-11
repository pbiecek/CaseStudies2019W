import cv2
import os
import face_recognition
import align_dataset_mtcnn
import classifier
import tensorflow as tf
import align.detect_face

def find_biggest_face(image):
    face_locations = face_recognition.face_locations(image)
    
    if len(face_locations) == 0:
        return None
    
    biggest = face_locations[0]
    for face_location in face_locations:
        top, right, bottom, left = face_location
        if (bottom - top) * (right - left) > (biggest[2] - biggest[0]) * (biggest[1] - biggest[3]):
            biggest = face_location
    return biggest

def draw_rectangle_on_image(image, coordinates):
    top, right, bottom, left = coordinates
    cv2.rectangle(image, (left, top), (right, bottom), (255,0,0), 2)

def draw_results_on_image(image, names, probabilities):
    cv2.rectangle(frame, (10, 10 + len(names) * 25), (250, 5), (0, 0, 255), cv2.FILLED)
    for i in range(len(names)):
        cv2.putText(image, names[i] + ': ' + str(round(probabilites[i], 3)), (20, 20 + i * 25), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

def align_photo(pnet, rnet, onet, image):
    return align_dataset_mtcnn.align_image(pnet, rnet, onet, image)

def classify(image, session):
    return classifier.classify(image, session)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

with tf.Graph().as_default():
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with sess.as_default():
        pnet, rnet, onet = align.detect_face.create_mtcnn(sess, None)

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

with tf.Graph().as_default():
    with tf.Session() as sess:
        classifier.load_models('models/20181214-040608.pb', 'models/my_classifier.pkl')
        while rval:
            face_location = find_biggest_face(frame)
            if face_location != None:
                top, right, bottom, left = face_location
                aligned = align_photo(pnet, rnet, onet, frame[top:bottom, left:right])
                if aligned is not None:
                    names, probabilites = classify(aligned, sess)
                    draw_results_on_image(frame, names, probabilites)
                draw_rectangle_on_image(frame, face_location)


            cv2.imshow('preview', frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break

cv2.destroyWindow("preview")
vc.release()

