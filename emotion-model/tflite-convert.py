import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file(
    "models/_mini_XCEPTION.134-0.66.hdf5")
tflite_model = converter.convert()
open("models/_mini_XCEPTION.134-0.66.tflite", "wb").write(tflite_model)
