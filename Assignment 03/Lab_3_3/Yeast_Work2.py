import arff
import numpy as np
import matplotlib.pyplot as plt
from heapq import nsmallest


trainDataset = arff.load(open('yeast_train.arff', 'rb'))
#data = np.array(dataset['data'])
#allData = list(dataset)

#print(trainDataset)
trainData = list(arff.load('yeast_train.arff'))
trainLen = len(trainData)
#print(trainData)
#print(trainLen)

testDataset = arff.load(open('yeast_test.arff', 'rb'))
testData = list(arff.load('yeast_test.arff'))
testLen = len(testData)
#print(testData)
#print(testLen)



classRank = []
for i in range(0,trainLen):
    if trainData[i][8] not in classRank:
        classRank.append(trainData[i][8])

#print(classRank)



#q =trainData[0][0]
#print(q)
#k = input('')
k1 = 1
k2 = 5
k3 = 10
k4 = 20
k5 = 30

#print(k1)

#print(trainData[445])



detected1 = []
detected2 = []
detected3 = []
detected4 = []
detected5 = []


predictionClassList1 = []
predictionClassList2 = []
predictionClassList3 = []
predictionClassList4 = []
predictionClassList5 = []

wrongCount1 = 0
wrongCount2 = 0
wrongCount3 = 0
wrongCount4 = 0
wrongCount5 = 0

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
    distance = []

    for yy in range(0,trainLen):
        distance.append([0] * 2)

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
        res1 = (s0 - r0) ** 2 + (s1 - r1) ** 2 + (s2 - r2) ** 2 + (s3 - r3) ** 2 + (s4 - r4) ** 2 + ( s5 - r5) ** 2 + (s6 - r6) ** 2 + (s7 - r7) ** 2
        #print(str(j) +"rq " + str(r1))
        res1 = np.sqrt(res1)

        distance[j][0] = res1
        distance[j][1] = r8


    distance.sort(key=lambda x: x[0])


#--------------------------------------------------------------- k1 ---------------------------------------------------
    k1ClassList = []
    for nv in range(0,k1):
        k1ClassList.append(distance[nv][1])

    #print(k1ClassList)

    k1UniqueClassList = []
    k1ClassFrequency = []

    for k in range(0, k1):
        k1ClassFrequency.append(0)

    for k in range(0,k1):
        if(k1ClassList[k] not in k1UniqueClassList):
            k1UniqueClassList.append(k1ClassList[k])

        kk = k1UniqueClassList.index(k1ClassList[k])
        k1ClassFrequency[kk] = k1ClassFrequency[kk] + 1

    #print(k1UniqueClassList)
    #print(k1ClassFrequency)
    mk = k1ClassFrequency[0]    #what is the highest frequency
    mkc = 1                     # how many have the highest frequency
    for k in range(1, k1):
        if k1ClassFrequency[k] > mk:
            mk = k1ClassFrequency[k]
            mkc = 1

        elif k1ClassFrequency[k] == mk:
            mkc = mkc + 1

    if mkc == 1:
        kk = k1ClassFrequency.index(mk)
        prediction = k1UniqueClassList[kk]
        # predictionClassList1.append(prediction)

    else:
        tempclasscheck = len(classRank) + 1
        for k in range(0, k1):
            if k1ClassFrequency[k] == mk:
                kkk = classRank.index(k1UniqueClassList[k])
                if tempclasscheck > kkk:
                    tempclasscheck = kkk
                    prediction = classRank[kkk]
        # predictionClassList1.append(prediction)

    predictionClassList1.append(prediction)
    if (s8 != prediction):
        wrongCount1 = wrongCount1 + 1
        #print("Wrong")


#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------ k2 ------------------------------------------------------
    k2ClassList = []
    for nv in range(0,k2):
        k2ClassList.append(distance[nv][1])

    #print(k2ClassList)

    k2UniqueClassList = []
    k2ClassFrequency = []

    for k in range(0, k2):
        k2ClassFrequency.append(0)

    for k in range(0,k2):
        if(k2ClassList[k] not in k2UniqueClassList):
            k2UniqueClassList.append(k2ClassList[k])

        kk = k2UniqueClassList.index(k2ClassList[k])
        k2ClassFrequency[kk] = k2ClassFrequency[kk] + 1

    #print(k2UniqueClassList)
    #print(k2ClassFrequency)
    mk = k2ClassFrequency[0]    #what is the highest frequency
    mkc = 1                     # how many have the highest frequency
    for k in range(1, k2):
        if k2ClassFrequency[k] > mk:
            mk = k2ClassFrequency[k]
            mkc = 1

        elif k2ClassFrequency[k] == mk:
            mkc = mkc + 1

    if mkc == 1:
        kk = k2ClassFrequency.index(mk)
        prediction = k2UniqueClassList[kk]
        # predictionClassList1.append(prediction)

    else:
        tempclasscheck = len(classRank) + 1
        for k in range(0, k2):
            if k2ClassFrequency[k] == mk:
                kkk = classRank.index(k2UniqueClassList[k])
                if tempclasscheck > kkk:
                    tempclasscheck = kkk
                    prediction = classRank[kkk]
        # predictionClassList1.append(prediction)

    predictionClassList2.append(prediction)
    if (s8 != prediction):
        wrongCount2 = wrongCount2 + 1
        #print("Wrong")


#-----------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------ k3 ------------------------------------------------------
    k3ClassList = []
    for nv in range(0,k3):
        k3ClassList.append(distance[nv][1])

    #print(k3ClassList)

    k3UniqueClassList = []
    k3ClassFrequency = []

    for k in range(0, k3):
        k3ClassFrequency.append(0)

    for k in range(0,k3):
        if(k3ClassList[k] not in k3UniqueClassList):
            k3UniqueClassList.append(k3ClassList[k])

        kk = k3UniqueClassList.index(k3ClassList[k])
        k3ClassFrequency[kk] = k3ClassFrequency[kk] + 1

    #print(k3UniqueClassList)
    #print(k3ClassFrequency)
    mk = k3ClassFrequency[0]    #what is the highest frequency
    mkc = 1                     # how many have the highest frequency
    for k in range(1, k3):
        if k3ClassFrequency[k] > mk:
            mk = k3ClassFrequency[k]
            mkc = 1

        elif k3ClassFrequency[k] == mk:
            mkc = mkc + 1

    if mkc == 1:
        kk = k3ClassFrequency.index(mk)
        prediction = k3UniqueClassList[kk]
        # predictionClassList1.append(prediction)

    else:
        tempclasscheck = len(classRank) + 1
        for k in range(0, k3):
            if k3ClassFrequency[k] == mk:
                kkk = classRank.index(k3UniqueClassList[k])
                if tempclasscheck > kkk:
                    tempclasscheck = kkk
                    prediction = classRank[kkk]
        # predictionClassList1.append(prediction)

    predictionClassList3.append(prediction)
    if (s8 != prediction):
        wrongCount3 = wrongCount3 + 1
        #print("Wrong")


#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------ k4 ------------------------------------------------------
    k4ClassList = []
    for nv in range(0,k4):
        k4ClassList.append(distance[nv][1])

    #print(k4ClassList)

    k4UniqueClassList = []
    k4ClassFrequency = []

    for k in range(0, k4):
        k4ClassFrequency.append(0)

    for k in range(0,k4):
        if(k4ClassList[k] not in k4UniqueClassList):
            k4UniqueClassList.append(k4ClassList[k])

        kk = k4UniqueClassList.index(k4ClassList[k])
        k4ClassFrequency[kk] = k4ClassFrequency[kk] + 1

    #print(k4UniqueClassList)
    #print(k4ClassFrequency)
    mk = k4ClassFrequency[0]    #what is the highest frequency
    mkc = 1                     # how many have the highest frequency
    for k in range(1, k4):
        if k4ClassFrequency[k] > mk:
            mk = k4ClassFrequency[k]
            mkc = 1

        elif k4ClassFrequency[k] == mk:
            mkc = mkc + 1

    if mkc == 1:
        kk = k4ClassFrequency.index(mk)
        prediction = k4UniqueClassList[kk]
        # predictionClassList1.append(prediction)

    else:
        tempclasscheck = len(classRank) + 1
        for k in range(0, k4):
            if k4ClassFrequency[k] == mk:
                kkk = classRank.index(k4UniqueClassList[k])
                if tempclasscheck > kkk:
                    tempclasscheck = kkk
                    prediction = classRank[kkk]
        # predictionClassList1.append(prediction)

    predictionClassList4.append(prediction)
    if (s8 != prediction):
        wrongCount4 = wrongCount4 + 1
        #print("Wrong")


#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------ k5 ------------------------------------------------------
    k5ClassList = []
    for nv in range(0,k5):
        k5ClassList.append(distance[nv][1])

    #print(k5ClassList)

    k5UniqueClassList = []
    k5ClassFrequency = []

    for k in range(0, k5):
        k5ClassFrequency.append(0)

    for k in range(0,k5):
        if(k5ClassList[k] not in k5UniqueClassList):
            k5UniqueClassList.append(k5ClassList[k])

        kk = k5UniqueClassList.index(k5ClassList[k])
        k5ClassFrequency[kk] = k5ClassFrequency[kk] + 1

    #print(k5UniqueClassList)
    #print(k5ClassFrequency)
    mk = k5ClassFrequency[0]    #what is the highest frequency
    mkc = 1                     # how many have the highest frequency
    for k in range(1, k5):
        if k5ClassFrequency[k] > mk:
            mk = k5ClassFrequency[k]
            mkc = 1

        elif k5ClassFrequency[k] == mk:
            mkc = mkc + 1

    if mkc == 1:
        kk = k5ClassFrequency.index(mk)
        prediction = k5UniqueClassList[kk]
        # predictionClassList1.append(prediction)

    else:
        tempclasscheck = len(classRank) + 1
        for k in range(0, k4):
            if k5ClassFrequency[k] == mk:
                kkk = classRank.index(k5UniqueClassList[k])
                if tempclasscheck > kkk:
                    tempclasscheck = kkk
                    prediction = classRank[kkk]
        # predictionClassList1.append(prediction)

    predictionClassList5.append(prediction)
    if (s8 != prediction):
        wrongCount5 = wrongCount5 + 1
        #print("Wrong")


#-----------------------------------------------------------------------------------------------------------------------




print(wrongCount1)
print(wrongCount2)
print(wrongCount3)
print(wrongCount4)
print(wrongCount5)

correct1 = testLen-wrongCount1
correct2 = testLen-wrongCount2
correct3 = testLen-wrongCount3
correct4 = testLen-wrongCount4
correct5 = testLen-wrongCount5


accuracy1 = correct1/testLen
accuracy2 = correct2/testLen
accuracy3 = correct3/testLen
accuracy4 = correct4/testLen
accuracy5 = correct5/testLen

xAxis = []
yAxis = []
xAxis.append(k1)
xAxis.append(k2)
xAxis.append(k3)
xAxis.append(k4)
xAxis.append(k5)

yAxis.append(accuracy1)
yAxis.append(accuracy2)
yAxis.append(accuracy3)
yAxis.append(accuracy4)
yAxis.append(accuracy5)
print(xAxis)
print(yAxis)

plt.plot(xAxis,yAxis)
plt.xlabel("K Value")
plt.ylabel("Accuracy")

plt.show()