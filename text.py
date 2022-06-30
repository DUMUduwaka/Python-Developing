'''
python file
'''
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10, 100)
y=x**3

plt.figure()
plt.plot(x,y,'-')
plt.title('Y vs X')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
