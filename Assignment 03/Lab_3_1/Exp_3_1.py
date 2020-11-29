#from scipy.io import arff
#import pandas as pd

#data = arff.loadarff('yeast_train.arff') #yeast_train.arff
#df = pd.DataFrame(data[0])

#df.head()
#print(df)
#print(df[1][1])
#-----------------------------------------------------------------------

import arff
import numpy as np
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


q =trainData[0][0]
print(q)
kt1, kt2, kt3 = input('').split()
k1 = int(kt1)
k2 = int(kt2)
k3 = int(kt3)
print(k1)
print(k2)
print(k3)

print(trainData[445])

knn1 = []
knn2 = []
knn3 = []

detected1 = []
detected2 = []
detected3 = []



wrongCount1 = 0

for i in range(0,testLen):
    s0 = testData[i][0]
    s1 = testData[i][1]
    s2 = testData[i][2]
    s3 = testData[i][3]
    s4 = testData[i][4]
    s5 = testData[i][5]
    s6 = testData[i][6]
    s7 = testData[i][7]
    s8 = testData[i][8]
    result1 = 9999999999999999999999999

    for j in range(0,trainLen):
        r0 = trainData[j][0]
        r1 = trainData[j][1]
        r2 = trainData[j][2]
        r3 = trainData[j][3]
        r4 = trainData[j][4]
        r5 = trainData[j][5]
        r6 = trainData[j][6]
        r7 = trainData[j][7]
        r8 = trainData[j][8]

        distance1 = []
        res1 = (s0 - r0) ** k1 + (s1 - r1) ** k1 + (s2 - r2) ** k1 + (s3 - r3) ** k1 + (s4 - r4) ** k1 + ( s5 - r5) ** k1 + (s6 - r6) ** k1 + (s7 - r7) ** k1
        #print(str(j) +"rq " + str(r1))
        res1 = np.exp(np.log(r1) / k1)

        if(res1<result1):
            cls1 = r8
            result1 = res1

    if(cls1 != s8):
        wrongCount1 = wrongCount1 + 1

    detected1.append(cls1)

print(wrongCount1)
#---------------------------------------------------------------k2

wrongCount2 = 0
for i in range(0,testLen):
    s0 = testData[i][0]
    s1 = testData[i][1]
    s2 = testData[i][2]
    s3 = testData[i][3]
    s4 = testData[i][4]
    s5 = testData[i][5]
    s6 = testData[i][6]
    s7 = testData[i][7]
    s8 = testData[i][8]
    result2 = 9999999999999999999999999

    for j in range(0,trainLen):
        r0 = trainData[j][0]
        r1 = trainData[j][1]
        r2 = trainData[j][2]
        r3 = trainData[j][3]
        r4 = trainData[j][4]
        r5 = trainData[j][5]
        r6 = trainData[j][6]
        r7 = trainData[j][7]
        r8 = trainData[j][8]
        res2 = (s0 - r0) ** k2 + (s1 - r1) ** k2 + (s2 - r2) ** k2 + (s3 - r3) ** k2 + (s4 - r4) ** k2 + ( s5 - r5) ** k2 + (s6 - r6) ** k2 + (s7 - r7) ** k2
        #print(str(i)+ " " +str(j) +"rq " + str(r1))
        res2 = np.exp(np.log(res2) / k2)

        if(res2<result2):
            cls2 = r8
            result2 = res2

    if(cls2 != s8):
        wrongCount2 = wrongCount2 + 1

    detected2.append(cls2)

print(wrongCount2)

#----------------------------------------------------------------------------------------- k3 ----------------

wrongCount3 = 0
for i in range(0,testLen):
    s0 = testData[i][0]
    s1 = testData[i][1]
    s2 = testData[i][2]
    s3 = testData[i][3]
    s4 = testData[i][4]
    s5 = testData[i][5]
    s6 = testData[i][6]
    s7 = testData[i][7]
    s8 = testData[i][8]
    result3 = 9999999999999999999999999

    for j in range(0,trainLen):
        r0 = trainData[j][0]
        r1 = trainData[j][1]
        r2 = trainData[j][2]
        r3 = trainData[j][3]
        r4 = trainData[j][4]
        r5 = trainData[j][5]
        r6 = trainData[j][6]
        r7 = trainData[j][7]
        r8 = trainData[j][8]
        res3 = (s0 - r0) ** k3 + (s1 - r1) ** k3 + (s2 - r2) ** k3 + (s3 - r3) ** k3 + (s4 - r4) ** k3 + ( s5 - r5) ** k3 + (s6 - r6) ** k3 + (s7 - r7) ** k3
        #print(str(i)+ " " +str(j) +"rq " + str(r1))
        res3 = np.exp(np.log(res3) / k3)

        if(res3<result3):
            cls3 = r8
            result3 = res3

    if(cls3 != s8):
        wrongCount3 = wrongCount3 + 1

    detected2.append(cls3)

print(wrongCount3)




