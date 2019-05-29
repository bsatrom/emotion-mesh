import tensorflow as tf

print(tf.__version__)

converter = tf.lite.TFLiteConverter.from_keras_model_file(
    "models/_mini_XCEPTION.134-0.66.hdf5")
# converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
converter.post_training_quantize = True
tflite_model = converter.convert()
open("models/_mini_XCEPTION.134-0.66-optimized.tflite", "wb").write(tflite_model)
