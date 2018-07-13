import numpy
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation, InputLayer
from keras.layers import Dropout, GlobalMaxPool1D
from keras.layers.convolutional import Conv1D, MaxPooling1D
from keras.callbacks import EarlyStopping
from vsyakaya_fignya import load_d

numpy.random.seed(42)

(x_train, y_train), (x_test, y_test) = load_d.load_data()
batch_size = 32
nb_classes = 2
nb_epoch = 25
img_rows, img_cols = 32, 32
img_channels = 3

model = Sequential()
# model.add(Conv1D(626333, 5, padding='same', input_shape=(None, 3131665), activation='relu'))
# model.add(Conv1D(626333, 5, activation='relu', padding='same'))
# model.add(MaxPooling1D(5))
# model.add(Dropout(0.25))
# model.add(Conv1D(104389, 6, padding='same', activation='relu'))
# model.add(Conv1D(104389, 6, activation='relu'))
# model.add(MaxPooling1D(6))
# model.add(InputLayer(input_shape=(None, 20275)))
model.add(Conv1D(20275, 5, padding='same', activation='relu', input_shape=(None, 20275)))
model.add(Conv1D(20275, 5, activation='relu'))
model.add(MaxPooling1D(5))
model.add(Conv1D(811, 5, padding='same', activation='relu'))
model.add(Conv1D(811, 5, activation='relu'))
# model.add(MaxPooling1D(5))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(200, activation='relu', input_shape=(None, 811)))
model.add(Dropout(0.4))
model.add(Dense(50, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(nb_classes, activation='softmax'))

early_stopping=EarlyStopping(monitor='val_loss')

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.summary()

model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=nb_epoch,
              validation_split=0.1,
              shuffle=True,
              verbose=2,
              callbacks=[early_stopping])

scores = model.evaluate(x_test, y_test, verbose=0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))