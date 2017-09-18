from keras.models import Sequential
from keras.layers import Dense

import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)


model = Sequential()
model.add(Dense(32, activation='relu', input_dim=784))
model.add(Dense(10, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.fit(mnist.train.images,mnist.train.labels)
print(model)


