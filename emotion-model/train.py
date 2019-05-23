import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.regularizers import l2
from tensorflow.keras.utils import plot_model

import pandas as pd
import numpy as np
import cv2
from PIL import Image
from sklearn.model_selection import train_test_split

import os
import matplotlib.pyplot as plt

# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# Load CSV Data
facesCsv = pd.read_csv("fer2013/fer2013.csv")
dataset = facesCsv.copy()

print(dataset.tail())

image_size = (48, 48)


def load_fer2013():
    data = dataset
    pixels = data['pixels'].tolist()
    width, height = 48, 48
    faces = []
    for pixel_sequence in pixels:
        face = [int(pixel) for pixel in pixel_sequence.split(' ')]
        face = np.asarray(face).reshape(width, height)
        face = cv2.resize(face.astype('uint8'), image_size)
        faces.append(face.astype('float32'))
    faces = np.asarray(faces)
    faces = np.expand_dims(faces, -1)
    #emotions = pd.get_dummies(data['emotion']).as_matrix()
    emotions = pd.get_dummies(data['emotion']).values
    return faces, emotions


def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0   
    return x


faces, emotions = load_fer2013()
faces = preprocess_input(faces)

xtrain, xtest, ytrain, ytest = train_test_split(
    faces, emotions, test_size=0.2, shuffle=True)

print("TRAIN Len: " + str(len(xtrain)))
print("TEST Len: " + str(len(xtest)))

# parameters
batch_size = 32
num_epochs = 150
input_shape = (48, 48, 1)
verbose = 1
num_classes = 7
patience = 50
base_path = 'models/'
l2_regularization = 0.01
dropout = 0.1

# data generator
data_generator = ImageDataGenerator(
    featurewise_center=False,
    featurewise_std_normalization=False,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=.1,
    horizontal_flip=True)

# model parameters
regularization = l2(l2_regularization)

# base input
inputs = tf.keras.layers.Input(input_shape)
x = tf.keras.layers.Conv2D(8, (3, 3), strides=(1, 1),
                           kernel_regularizer=regularization, use_bias=False)(inputs)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Activation('relu')(x)
# Added dropout to prevent overfitting
x = tf.keras.layers.Dropout(dropout)(x)
x = tf.keras.layers.Conv2D(8, (3, 3), strides=(1, 1),
                           kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Activation('relu')(x)

# layer 1
residual = tf.keras.layers.Conv2D(16, (1, 1), strides=(
    2, 2), padding='same', use_bias=False)(x)
residual = tf.keras.layers.BatchNormalization()(residual)
x = tf.keras.layers.SeparableConv2D(16, (3, 3), padding='same',
                                    kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Activation('relu')(x)
# Added dropout to prevent overfitting
x = tf.keras.layers.Dropout(dropout)(x)
x = tf.keras.layers.SeparableConv2D(16, (3, 3), padding='same',
                                    kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)
x = tf.keras.layers.add([x, residual])

# layer 2
residual = tf.keras.layers.Conv2D(32, (1, 1), strides=(
    2, 2), padding='same', use_bias=False)(x)
residual = tf.keras.layers.BatchNormalization()(residual)
x = tf.keras.layers.SeparableConv2D(32, (3, 3), padding='same',
                                    kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Activation('relu')(x)
# Added dropout to prevent overfitting
x = tf.keras.layers.Dropout(dropout)(x)
x = tf.keras.layers.SeparableConv2D(32, (3, 3), padding='same',
                                    kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)
x = tf.keras.layers.add([x, residual])

# layer 3
residual = tf.keras.layers.Conv2D(64, (1, 1), strides=(
    2, 2), padding='same', use_bias=False)(x)
residual = tf.keras.layers.BatchNormalization()(residual)
x = tf.keras.layers.SeparableConv2D(64, (3, 3), padding='same',
                                    kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Activation('relu')(x)
# Added dropout to prevent overfitting
x = tf.keras.layers.Dropout(dropout)(x)
x = tf.keras.layers.SeparableConv2D(64, (3, 3), padding='same',
                                    kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)
x = tf.keras.layers.add([x, residual])

# layer 4
residual = tf.keras.layers.Conv2D(128, (1, 1), strides=(
    2, 2), padding='same', use_bias=False)(x)
residual = tf.keras.layers.BatchNormalization()(residual)
x = tf.keras.layers.SeparableConv2D(128, (3, 3), padding='same',
                                    kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Activation('relu')(x)
# Added dropout to prevent overfitting
x = tf.keras.layers.Dropout(dropout)(x)
x = tf.keras.layers.SeparableConv2D(128, (3, 3), padding='same',
                                    kernel_regularizer=regularization, use_bias=False)(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)
x = tf.keras.layers.add([x, residual])

x = tf.keras.layers.Conv2D(num_classes, (3, 3), padding='same')(x)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
outputs = tf.keras.layers.Activation('softmax', name='predictions')(x)

model = tf.keras.models.Model(inputs, outputs)
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary() 
plot_model(model, to_file='results/model_architecture.png', show_shapes=True, show_layer_names=True)

# callbacks
log_file_path = base_path + '_emotion_training.log'
csv_logger = tf.keras.callbacks.CSVLogger(log_file_path, append=False)
early_stop = tf.keras.callbacks.EarlyStopping('val_loss', patience=patience)
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    'val_loss', factor=0.1, patience=int(patience/4), verbose=1)
trained_models_path = base_path + '_mini_XCEPTION'
model_names = trained_models_path + '.{epoch:02d}-{val_acc:.2f}.hdf5'
model_checkpoint = tf.keras.callbacks.ModelCheckpoint(
    model_names, 'val_loss', verbose=1, save_best_only=True)
callbacks = [model_checkpoint, csv_logger, early_stop, reduce_lr]

history = model.fit_generator(data_generator.flow(xtrain, ytrain, batch_size),
                              steps_per_epoch=len(xtrain) / batch_size,
                              epochs=num_epochs, verbose=1, callbacks=callbacks,
                              validation_data=(xtest, ytest))

# visualize the training results
acc = history.history['acc']
val_acc = history.history['val_acc']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(num_epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
