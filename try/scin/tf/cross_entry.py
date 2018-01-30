import numpy as np
from matplotlib import pyplot as plt

y=0.9
d = np.linspace(-y,1-y,100)
a=y+d

zz = -(y*np.log(a)+(1-y)*np.log(1-a) )

plt.plot(d,zz)

plt.show()