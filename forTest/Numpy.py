#%% Array
import numpy as np

a= np.array([1,2,3])
b= np.array([[1,2],[3,4]])    # 2d
c= np.array([1,2,3,4,5],ndmin=2)    # [[1 2 3 4 5]]
d= np.array([1,2,3],dtype=float)    # [1. 2. 3.]

#%% Array Creation arange�� arr. range��ŭ �����´� �����ϸ�ȴ�.
import numpy as np
a = np.arange(5)    # [0 1 2 3 4]
b = np.arange(3,9,2)    # [3 5 7]    
                        #c = .zeros(5) .ones(5)
c = np.eye(3)   # I 3
d = np.eye(3,4) # I 3x4
e = np.linspace(10,20,5)    # [10. 12.5 15. 17.5 20.] 10���� 20���� 5�����ϱ�

#%% Changing Shape
import numpy as np

a = np.arange(6)
print(a)
b = a.reshape(3,2)
np.shape(b) # (3,2)
np.size(b)  # element ����?
np.ndim(b)  # ����?
np.transpose(b) 

c = np.copy(b)  # ���� 
np.ravel(b) # 1d �� �ٲٱ� []

# ��ĳ��� dot ����� inner���굵 ���� np.inner(a,b)

#%% Random
import numpy as np
b = np.random.rand(3,2) # 3x2 (0~1)���� ������ ��� �����
c = np.random.randint(3,9,size=(2,4))   # 3~8 int�� 2x4�����
print(b)
print(c)