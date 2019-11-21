from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Convolution2D, MaxPooling2D, Dropout, Flatten, Reshape
from keras import optimizers
import numpy as np

x_train = np.array([ [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0,-1, 1, 0, 0, 0,],
                [0, 0, 0, 1,-1, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],])
x_train = x_train.reshape(1,1,8,8)

y_train = np.array([ [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 1, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0,0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],])
y_train = y_train.reshape(1,1,8,8)

model = Sequential()
model.add(Convolution2D(32, 5, 5, border_mode = 'same', input_shape=(1, 8, 8), activation='relu'))
model.add(MaxPooling2D(pool_size =(2,2), dim_ordering="th"))
model.add(Convolution2D(16,3,3, border_mode ='same', activation ='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="th"))
model.add(Convolution2D(16,3,3, border_mode ='same', activation ='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="th"))

#do i need a flattern layer here?
model.add(Flatten())
model.add(Dense(16, activation='relu'))
model.add(Dense(60 , init ='normal'))
'''
model.add(Activation('softmax'))'''
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=10)