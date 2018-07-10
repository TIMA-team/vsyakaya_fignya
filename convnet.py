def cnn_model(x_train_data, keep_rate=0.1):
    with tf.name_scope("counter1"):
        data = tf.layers.conv1d(inputs=x_train_data, filters=2, kernel_size=3, strides=1, padding='same',
                                activation=tf.nn.relu)
        data = tf.layers.max_pooling1d(inputs=data, pool_size=2, strides=2)
        data = tf.nn.embedding_lookup_sparse(inputs=data,)  # ??????????????)
        data=tf.layers.dense(inputs=data)#, )
        # хуй короч знает что тут я в призду
#def cnn4_model:
