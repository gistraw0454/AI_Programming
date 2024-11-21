#%% test1
import numpy as np

np.array([1,2,3])
np.array([[1,2,3],[4,5,6]])
np.array(range(5))
np.array([i for i in range(10,100)])
# %% test2
np.arange(5,10) # 이걸로 5~9까지를 만들 수 있다.
list(range(5,10))

np.zeros(5) # 0이 5개로 채워지는 1d arr반환

np.ones(5)

#%% test 3
arr= np.zeros((5,5))    #shape
print(arr)

#%% test 4
np.zeros_like(arr)  # arr data


#%% test 5
np.eye(3)   # I반환

#%% test 6
np.diag([1,2,3 ])   #외울필요없고 그때그때 이런게있구나 쓰면됨 대각행렬 반환

#%% test 7 이둘의 차이를 잘 알아두자 !!!!!!!!!!!!!!!!!!!!
print(np.linspace(10,20,5))
print(np.arange(10,20,5))


#%% test 8 
arr = np.arange(1,5)  # 1d

np.arange(1,5).reshape((2,2))   # 2d 로 변경
np.arange(1,5).reshape((2,2,1)) # 3d 로 변경
# 계산할수있는 element개수와 앞의 elemnet개수가연산가능해야함

#%% reshape말고 shpae바꿔주는 함수
arr.flatten()

arr.transpose()

#%% matrix 연산
arr2 = arr*2

# np.dot
# np.inner

#%% dot vs inner

arr1 = np.arange(0,4).reshape((2,2))
arr2 = np.arange(4,8).reshape((2,2))

print(arr1,arr2)

print("\n")
print(np.dot(arr1,arr2))    # 2d가되면  matrix multiplication 
print(np.inner(arr1,arr2))  # 2d라고해도  vectorwise하게 dot 진행

#%% 임의의 숫자를 출력하여 반올림
arr = np.random.rand(5)

print(arr)
print(np.around(arr,3)) #소숫점3까지 반올림 수행
0
#%% 
arr = np.random.rand(5)
print(np.average(arr))
print(np.std(arr))
print(np.var(arr))

#%% submodule 주로쓰는 rand

print(np.random.rand(5))    # uniform [0,1]
print(np.random.randn(5))   # normal확률분포로 난수 생성
print(np.random.randint(0,10,size = 5)) # 0부터 10까지의 숫자를 5개 생성하라
