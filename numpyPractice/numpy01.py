#%% test1
import numpy as np

np.array([1,2,3])
np.array([[1,2,3],[4,5,6]])
np.array(range(5))
np.array([i for i in range(10,100)])
# %% test2
np.arange(5,10) # �̰ɷ� 5~9������ ���� �� �ִ�.
list(range(5,10))

np.zeros(5) # 0�� 5���� ä������ 1d arr��ȯ

np.ones(5)

#%% test 3
arr= np.zeros((5,5))    #shape
print(arr)

#%% test 4
np.zeros_like(arr)  # arr data


#%% test 5
np.eye(3)   # I��ȯ

#%% test 6
np.diag([1,2,3 ])   #�ܿ��ʿ���� �׶��׶� �̷����ֱ��� ����� �밢��� ��ȯ

#%% test 7 �̵��� ���̸� �� �˾Ƶ��� !!!!!!!!!!!!!!!!!!!!
print(np.linspace(10,20,5))
print(np.arange(10,20,5))


#%% test 8 
arr = np.arange(1,5)  # 1d

np.arange(1,5).reshape((2,2))   # 2d �� ����
np.arange(1,5).reshape((2,2,1)) # 3d �� ����
# ����Ҽ��ִ� element������ ���� elemnet���������갡���ؾ���

#%% reshape���� shpae�ٲ��ִ� �Լ�
arr.flatten()

arr.transpose()

#%% matrix ����
arr2 = arr*2

# np.dot
# np.inner

#%% dot vs inner

arr1 = np.arange(0,4).reshape((2,2))
arr2 = np.arange(4,8).reshape((2,2))

print(arr1,arr2)

print("\n")
print(np.dot(arr1,arr2))    # 2d���Ǹ�  matrix multiplication 
print(np.inner(arr1,arr2))  # 2d����ص�  vectorwise�ϰ� dot ����

#%% ������ ���ڸ� ����Ͽ� �ݿø�
arr = np.random.rand(5)

print(arr)
print(np.around(arr,3)) #�Ҽ���3���� �ݿø� ����
0
#%% 
arr = np.random.rand(5)
print(np.average(arr))
print(np.std(arr))
print(np.var(arr))

#%% submodule �ַξ��� rand

print(np.random.rand(5))    # uniform [0,1]
print(np.random.randn(5))   # normalȮ�������� ���� ����
print(np.random.randint(0,10,size = 5)) # 0���� 10������ ���ڸ� 5�� �����϶�
