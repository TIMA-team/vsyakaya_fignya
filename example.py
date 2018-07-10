import tensorflow as tf


data = tf.layers.conv1d(inputs=x_train_data, filters=2, kernel_size=3, strides = 1, padding='same', activation=tf.nn.relu)
data = tf.layers.max_pooling1d(inputs=data,pool_size=2,strides=2)
