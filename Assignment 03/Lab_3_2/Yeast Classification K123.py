import arff
import numpy as np
from heapq import nsmallest


trainDataset = arff.load(open('yeast_train.arff', 'rb'))
#data = np.array(dataset['data'])
#allData = list(dataset)

print(trainDataset)
trainData = list(arff.load('yeast_train.arff'))
trainLen = len(trainData)
print(trainData)
print(trainLen)

testDataset = arff.load(open('yeast_test.arff', 'rb'))
testData = list(arff.load('yeast_test.arff'))
testLen = len(testData)
print(testData)
print(testLen)


classRank = []
for i in range(0,trainLen):
    if trainData[i][8] not in classRank:
        classRank.append(trainData[i][8])

print(classRank)

kt1, kt2, kt3 = input('').split()
k1 = int(kt1)
k2 = int(kt2)
k3 = int(kt3)
print(k1)
print(k2)
print(k3)

print(trainData[445])



detected1 = []
detected2 = []
detected3 = []

predictionClassList1 = []
predictionClassList2 = []
predictionClassList3 = []

wrongCount1 = 0
wrongCount2 = 0
wrongCount3 = 0


for i in range(0,trainLen):
    s0 = testData[i][0]
    s1 = testData[i][1]
    s2 = testData[i][2]
    s3 = testData[i][3]
    s4 = testData[i][4]
    s5 = testData[i][5]
    s6 = testData[i][6]
    s7 = testData[i][7]
    s8 = testData[i][8]
    distance = []

    for j in range(0, trainLen):
        if(j != i):
            r0 = trainData[j][0]
            r1 = trainData[j][1]
            r2 = trainData[j][2]
            r3 = trainData[j][3]
            r4 = trainData[j][4]
            r5 = trainData[j][5]
            r6 = trainData[j][6]
            r7 = trainData[j][7]
            r8 = trainData[j][8]
            res1 = (s0 - r0) ** 2 + (s1 - r1) ** 2 + (s2 - r2) ** 2 + (s3 - r3) ** 2 + (s4 - r4) ** 2 + (
                        s5 - r5) ** 2 + (s6 - r6) ** 2 + (s7 - r7) ** 2
            # print(str(j) +"rq " + str(r1))
            res1 = np.sqrt(res1)

            distance.append(res1)

detectedFinal = []


predictionClassListFinal = []

wrongCountFinal = 0
