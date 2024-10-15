#%% 시각화해주는 코드이구나 하고 넘어가보자.
from matplotlib import pyplot as plt
import numpy as np


#%% ex1
def gaussian(x):
    return lambda x: np.exp(-(0.5-x)**2/1.5)

x= np.arange(-2,2.5,0.01)

y = gaussian(x)

print(len(x))
print(len(y))

plt.plot(x,y)
plt.show()