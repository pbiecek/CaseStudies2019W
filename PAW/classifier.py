# MIT License
# 
# Copyright (c) 2016 David Sandberg
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import argparse
import facenet
import os
import sys
import math
import pickle
from sklearn.svm import SVC
from operator import itemgetter

model = None
class_names = None

def classify(image, sess): 
    global model, class_names          
    np.random.seed(seed=np.sum(image))           
            
    # Get input and output tensors
    images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
    embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
    phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
    embedding_size = embeddings.get_shape()[1]
            
    # Run forward pass to calculate embeddings
    print('Calculating features for image')
    emb_array = np.zeros((1, embedding_size))

    images = np.zeros((1, 160, 160, 3))
        
    if image.ndim == 2:
        image = facenet.to_rgb(image)
    image = facenet.prewhiten(image)
    image = facenet.crop(image, False, 160)
    image = facenet.flip(image, False)
    images[0,:,:,:] = image

    feed_dict = { images_placeholder:images, phase_train_placeholder:False }
    emb_array[0:1,:] = sess.run(embeddings, feed_dict=feed_dict)
            
    ###
    predictions = model.predict_proba(emb_array)[0]
    best_class_indices = ind = np.argpartition(predictions, -3)[-3:]
    best_class_indices = best_class_indices[np.argsort(predictions[best_class_indices])][::-1]
    best_class_probabilities = predictions[best_class_indices]
    
    return np.array(class_names)[best_class_indices], best_class_probabilities           

    #for i in range(len(best_class_indices)):
    #    print('%4d  %s: %.3f' % (i, class_names[best_class_indices[i]], best_class_probabilities[i]))  

def load_models(embeddings_model_path, classifier_path): 
    # Load the model
    print('Loading feature extraction model')
    facenet.load_model(embeddings_model_path) 

    classifier_filename_exp = os.path.expanduser(classifier_path)
                
    # Classify images
    print('Testing classifier')
    global model, class_names
    with open(classifier_filename_exp, 'rb') as infile:
        (model, class_names) = pickle.load(infile)

    print('Loaded classifier model from file "%s"' % classifier_filename_exp)
