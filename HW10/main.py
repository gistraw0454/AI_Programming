import numpy as np

def main():
    ml = ML()
    fileName = input("Enter the file name of training data: ")
    ml.setData('train', fileName)
    fileName = input("Enter the file name of test data: ")
    ml.setData('test', fileName)
    ml.buildModel()
    ml.testModel()
    ml.report()

class ML:
    def __init__(self):
        self._trainDX = np.array([]) # Feature value matrix (training data)
        self._trainDy = np.array([]) # Target column (training data)
        self._testDX = np.array([])  # Feature value matrix (test data)
        self._testDy = np.array([])  # Target column (test data)
        self._testPy = np.array([])  # Predicted values for test data
        self._rmse= 0          # Root mean squared error
        self._aType = 0        # Type of learning algoritm
        self._w = np.array([]) # Optimal weights for linear regression
        self._k = 0            # k value for k-NN

    def setData(self, dtype, fileName): # set class variables
        XArray, yArray = self.createMatrices(fileName)
        if dtype == 'train':
            self._trainDX = XArray
            self._trainDy = yArray
        elif dtype == 'test':
            self._testDX = XArray
            self._testDy = yArray
            self._testPy = np.zeros(np.size(yArray)) # Initialize to all 0
            
    def createMatrices(self, fileName): # Read data from file and make arrays
        infile = open(fileName, 'r')
        XSet = []
        ySet = []
        for line in infile:
            data = [float(x) for x in line.split(',')]
            features = data[0:-1]
            target = data[-1]
            XSet.append(features)
            ySet.append(target)
        infile.close()
        XArray = np.array(XSet)
        yArray = np.array(ySet)
        return XArray, yArray

    def buildModel(self):
        print()
        print("Which learning algorithm do you want to use?")
        print(" 1. Linear Regression")
        print(" 2. k-NN")
        aType = int(input("Enter the number: "))
        self._aType = aType
        if aType == 1:
            self._w = self.linearRegression()
        elif aType == 2:
            self._k = int(input("Enter the value for k: "))

    def linearRegression(self): # Do linear regression and return optimal w 
        X = self._trainDX
        n = np.size(self._trainDy)
        X0 = np.ones([n, 1])
        nX = np.hstack((X0, X)) # Add a column of all 1's as the first column
        y = self._trainDy
        t_nX = np.transpose(nX)
        return np.dot(np.dot(np.linalg.inv(np.dot(t_nX, nX)), t_nX), y)
        

    def testModel(self):
        n = np.size(self._testDy)
        if self._aType == 1:
            self.testLR(n)
        elif self._aType == 2:
            self.testKNN(n)

    def testLR(self, n): # Test linear regression with the test set
        for i in range(n):
            self._testPy[i] = self.LR(self._testDX[i])
 
    def LR(self, data): # Apply linear regression to a test data
        nData = np.insert(data, 0, 1)
        return np.inner(self._w, nData)
        
    def testKNN(self, n): # Apply k-NN to the test set
        for i in range(n):
            self._testPy[i] = self.kNN(self._testDX[i])

    ### Implement the following and other necessary methods
    def kNN(self, query):
            closestK = self.findCK(query)   # query와 가장 가까운 k 배열을 찾고
            predict = self.takeAvg(closestK)    # 그 배열을 돌면서 최적의 list를 뱉어낸다.
            return predict

    def findCK(self,query):
        m = np.size(self._trainDy)  # m에 대한 list 만들기
        k = self._k
        closestK = np.arange(2*k).reshape(k,2)  # closestK 를 초기화한다.
        for i in range(k):  # k까지는 초기화
            closestK[i,0] = i
            closestK[i,1] = self.sDistance(self._trainDX[i],query)
        for i in range(k,m):    # k+1 부터는 업데이트시킬 값을 계속 계산하며 넣어준다.
            self.updateCK(closestK,i,query)
        return closestK

    def sDistance(self, dataA, dataB):
        dim = np.size(dataA)
        sumOfSquares = 0
        for i in range(dim):
            sumOfSquares += (dataA[i] - dataB[i])**2    # 두 점사이 거리 = x끼리 y끼리 z끼리 빼고 제곱한 후 더하기
        return sumOfSquares            

    def updateCK(self,closestK, i, query):
        # distance가 가장 먼 index를 j에 넣어주기
        # i번째 거리를 비교해주면서 해당 거리가 더 가까우면 j에 넣어준다.
        # 전체에 대해 해당 쿼리가 가장 가까운 k개의 결과를 받을수있다.
        d = self.sDistance(self._trainDX[i], query)
        j = np.argmax(closestK[:, 1])
        if closestK[j, 1] > d:
            closestK[j, 0] = i
            closestK[j, 1] = d

    def takeAvg(self, closestK):
        k = self._k
        total = 0
        for i in range(k):
            j = closestK[i,0]
            total += self._trainDy[j]
        return total/k
    
    def report(self):
        self.calcRMSE()
        print()
        print("RMSE: ", round(self._rmse, 2))

    def calcRMSE(self):
        n = np.size(self._testDy) # Number of test data
        totalSe = 0
        for i in range(n):
            se = (self._testDy[i] - self._testPy[i]) ** 2
            totalSe += se
        self._rmse = np.sqrt(totalSe) / n


main()
