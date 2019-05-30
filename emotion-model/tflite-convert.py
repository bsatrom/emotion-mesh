import tensorflow as tf

print(tf.__version__)

file = "models/_mini_XCEPTION.01-0.40-quantized"

converter = tf.lite.TFLiteConverter.from_keras_model_file(
    file + ".hdf5")

# converter.post_training_quantize = True
tflite_model = converter.convert()
open(file + "-optimized.tflite", "wb").write(tflite_model)
