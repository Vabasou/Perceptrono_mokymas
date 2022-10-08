import math
import matplotlib.pyplot as plt
import numpy as np

EPOCHS = 100
LEARN_TEST_RATION = 80
RANDOM_WEIGHT = 0.123456789

def learningPhase(learnData, testData, activationFunction, learningRate):
    positives = []
    cost = []
    lineLength = getLineLength(learnData[0])
    print(lineLength)
    w = fillWeights(lineLength)
    # print(w)
    for i in range(EPOCHS):
        for learnLine in learnData:
            x, t = getLineData(learnLine)
            y = chooseFunction(activationFunction, getA(x, w))
            if (y != t):
                w = calculateAdaline(w, x, t, y, learningRate)
        positive, error = testingPhase(w, learnData, activationFunction)
        positives.append(positive)
        cost.append(round(error, 3))
    return positives, cost, w
        
def testingPhase(w, testData, activationFunction):
    count = 0
    cost = 0
    for testLine in testData:
        x, t = getLineData(testLine)
        y = chooseFunction(activationFunction, getA(x, w))
        if (round(y) == int(t)):
            count += 1
        else:
            cost += pow(y - t, 2)
    return ((count / len(testData)) * 100), cost

# Helper functions

def stepActivationFunction(a):
    if (a >= 0):
        return 1
    else:
        return 0

def sigmoidActivationFunction(a):
    return (1 / (1 + math.exp(-a)))

def chooseFunction(number, a):
    if (number == 0):
        return stepActivationFunction(a)
    else:
        return sigmoidActivationFunction(a)
   
def getFileData(fileName):
    f = open(fileName)
    lines = f.read().splitlines()
    f.close()
    length = len(lines)
    index = round((LEARN_TEST_RATION * length) / 100)
    learnData = lines[0:index]
    testData = lines[index:]
    return  learnData, testData

def getLineData(line):
    x = [1]
    dataList = str(line).split(',')
    t = float(dataList[-1])
    for object in range(len(dataList) - 1):
        x.append(float(dataList[object]))
    return x, t

def getLineLength(line):
    li = str(line).split(",")
    return len(li)

def calculateAdaline(w, x, t, y, learningRate):
    newWeights = []
    for i in range(len(w)):
        newWeights.append(round(float(w[i]) + learningRate * (float(t) - float(y)) * float(x[i]), 4))
    return newWeights

def fillWeights(lineLength):
    rowWeights = []
    for i in range(lineLength):
        rowWeights.append(RANDOM_WEIGHT)
    return rowWeights

def getA(x, w):
    result = 0
    for i in range(len(x)):
        result += float(x[i]) * float(w[i])
    return result

# Plot

def plotGraph(value, ylabel):
    x = np.arange(0, EPOCHS)
    y = value
    
    fig, ax = plt.subplots()
    
    ax.set_ylim(ymin=0, ymax=100)
    ax.set_xlim(xmin=0, xmax=100)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Epochų skaičius")
    ax.plot(x, y)
    
    plt.show()
    
def plotLearningGraph(data1, data2, data3, yLabel):
    x = np.arange(0, EPOCHS)
    y = data1
    z = data2
    b = data3
    
    fig, ax = plt.subplots()
    
    ax.plot(x, y, label='0,001')
    ax.plot(x, z, label='0,01')
    ax.plot(x, b, label='0,1')

    ax.set_ylabel(yLabel)
    ax.set_xlabel("Epochų skaičius")
    
    ax.legend()
    plt.show()
    
def main():
    learningRate = 0.001
    files = ['correct_iris.txt', 'correct_breast_cancer.txt']
    
    for file in files:
        learnData, testData = getFileData(file)
        print(str(file))
        for i in range(2):
            positives, cost, w = learningPhase(learnData, testData, i, learningRate)
            print("Aktyvacijos funkcija: " + str(i))            
            print("Positives")
            print(positives[-1])
            print("Negatives")
            print(cost[-1])
            print("Weights")
            print(w)
            plotGraph(positives, "Tikslumas (%)")
            plotGraph(cost, "Paklaida")
            print("-------------------------------") 
            
    learnData, testData = getFileData(files[1])
    positives1, cost1, w1 = learningPhase(learnData, testData, i, learningRate)
    positives2, cost2, w2 = learningPhase(learnData, testData, i, learningRate * 10)
    positives3, cost3, w3 = learningPhase(learnData, testData, i, learningRate * 100)
    
    plotLearningGraph(positives1, positives2, positives3, "Tikslumas (%)")
    plotLearningGraph(cost1, cost2, cost3, "Paklaida")    
    
if __name__ == "__main__":
    main()