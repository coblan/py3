import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

x= np.linspace(-1, 1, num=100)
y= 0.5*x +7
#plt.plot(x,y)
#plt.show()

#x = tf.convert_to_tensor(x,dtype=tf.float32)
#y= tf.convert_to_tensor(y,dtype=tf.float32)

x_i = tf.placeholder(tf.float32)
y_i= tf.placeholder(tf.float32)

w = tf.Variable(0,dtype=tf.float32)
b = tf.Variable(0,dtype=tf.float32)

y_o= tf.multiply(w,x_i)+ b
loss = tf.reduce_mean(tf.square(y_i-y_o))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init = tf.global_variables_initializer()
sess =tf.Session()
sess.run(init)
ls =[]
for i in range(200):
    sess.run(train_step,{x_i:x,y_i:y})
    print(sess.run([w,b,loss], {x_i:x,y_i:y}))
    ls.append(sess.run(loss,{x_i:x,y_i:y}))
    
plt.plot(ls)
plt.show()
