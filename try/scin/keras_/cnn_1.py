from keras.optimizers import Adadelta
from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Dropout,Flatten

import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)

batch_size = 500
num_classes = 10
epochs = 12

x_train=mnist.train.images.reshape(-1,28,28,1)
y_train= mnist.train.labels

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(28,28,1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=Adadelta(),
              metrics=['accuracy'])


model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,)
print(model)


