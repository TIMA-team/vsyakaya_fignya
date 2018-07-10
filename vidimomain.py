import tensorflow as tf
import numpy as np
import matplotlib as plt
import os
import random
with tf.name_scope('inputs'):
    x_input = tf.placeholder(tf.float32, shape=[None, vc1num])
    y_input = tf.placeholder(tf.float32, shape=[None, 2])

dir = ''
train_dir = dir + 'train'
test_dir = dir + 'test'
(x_train, y_train) = get_data(train_dir, 5)
(x_test, y_test) = get_data(test_dir, 5)


train_neural_network(x_train, y_train, x_test, y_test, epochs=10, batch_size=1, learning_rate=0.3)