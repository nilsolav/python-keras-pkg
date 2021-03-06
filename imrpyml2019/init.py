from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

import os, pkg_resources

# For reproducibility
from numpy.random import seed
from tensorflow import set_random_seed

def train():

    # Set seed
    seed(1)
    set_random_seed(2)

    print(tf.__version__)
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
            loss=keras.losses.sparse_categorical_crossentropy,
            metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=7)

    print('Saving model')

    filepath = os.path.dirname(os.path.realpath(__file__))
    modelpath = filepath + '/my_model.h5'
    model.save(modelpath)

    print('Model saved to:' + filepath + '/my_model.h5')

    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Test accuracy:', test_acc)

    return test_acc
