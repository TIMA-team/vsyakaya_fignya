import math
import tensorflow as tf
import numpy as np
from vsyakaya_fignya import line_to_v


def generate_batch(b_size):
  batch = np.ndarray(shape=(b_size), dtype=np.int32)
  labels = np.ndarray(shape=(b_size, 1), dtype=np.int32)
  # tf.sparse_tensor_to_dense() ?
  # line_to_v.get_second_sparse_vec()
  print('batch generation not implemented!')
  exit(-1)
  return batch, labels


vocabulary_size = 20275
embedding_size = 15
batch_size = 128
graph = tf.Graph()

with graph.as_default():
    embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
    nce_weights = tf.Variable(tf.truncated_normal([vocabulary_size, embedding_size],
                                                  stddev=1.0 / math.sqrt(embedding_size)))
    nce_biases = tf.Variable(tf.zeros([vocabulary_size]))
    train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
    train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
    embed = tf.nn.embedding_lookup(embeddings, train_inputs)
    loss = tf.reduce_mean(tf.nn.nce_loss(weights=nce_weights,
                                         biases=nce_biases,
                                         labels=train_labels,
                                         inputs=embed,
                                         num_sampled=64,
                                         num_classes=vocabulary_size))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)
    saver = tf.train.Saver()
    # писАть и писАть


with tf.Session(graph=graph) as session:
    # писАть и писАть
    saver.save(session, 'embeddings_model.ckpt')
