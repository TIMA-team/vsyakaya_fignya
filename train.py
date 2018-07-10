import tensorflow as tf


def train_neural_network(x_train_data, y_train_data, x_test_data, y_test_data, learning_rate=0.05, keep_rate=0.7,
                         epochs=10, batch_size=32):
    with tf.name_scope("cross_entropy"):  # wtf is x_ and y_ inputs?
        prediction = convert.cnn_model(x_input, keep_rate, seed=1)
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
            logits=prediction, labels=y_input))

    with tf.name_scope("training"):
        optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

    correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y_input, 1))
    accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

    iterations = int(len(x_train_data) / batch_size)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        import datetime

        start_time = datetime.datetime.now()

        iterations = int(len(x_train_data) / batch_size)
        # run epochs
        for epoch in range(epochs):
            start_time_epoch = datetime.datetime.now()
            print('Epoch', epoch, 'started', end='')
            epoch_loss = 0
            # mini batch
            for itr in range(iterations):
                mini_batch_x = x_train_data[itr * batch_size: (itr + 1) * batch_size]
                mini_batch_y = y_train_data[itr * batch_size: (itr + 1) * batch_size]
                _optimizer, _cost = sess.run([optimizer, cost],
                                             feed_dict={x_input: mini_batch_x, y_input: mini_batch_y})
                epoch_loss += _cost

            acc = 0
            itrs = int(len(x_test_data) / batch_size)
            for itr in range(itrs):
                mini_batch_x_test = x_test_data[itr * batch_size: (itr + 1) * batch_size]
                mini_batch_y_test = y_test_data[itr * batch_size: (itr + 1) * batch_size]
                acc += sess.run(accuracy, feed_dict={x_input: mini_batch_x_test, y_input: mini_batch_y_test})

            end_time_epoch = datetime.datetime.now()
            print(' Testing Set Accuracy:', acc / itrs, ' Time elapse: ',
                  str(end_time_epoch - start_time_epoch))

        end_time = datetime.datetime.now()
        print('Time elapse: ', str(end_time - start_time))