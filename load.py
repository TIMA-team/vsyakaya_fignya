import os
import numpy as np
import random


def get_data(data_set, amount_of_data_needed):
    global sess
    global n_classes
    parties = []
    for s in os.listdir("mlboot_daraset/" + data_set):
        '''
        тут кусок кода как подавать данные
        точнее как их лейбелить
        '''
    x_data=[]
    y_data=[]
    random.shuffle(parties)
    for x,y in parties[:amount_of_data_needed]:
        '''
        как их выгружать будем
        '''
        y_data.append(y)
        x_data.append()
    return np.asarray(x_data, dtype=np.float32), to_categorical(y_data, n_classes)  # to_categorical?

