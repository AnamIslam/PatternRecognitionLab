import arff
import numpy as np
from heapq import nsmallest

trainDataset = arff.load(open('yeast_train.arff', 'rb'))
# data = np.array(dataset['data'])
# allData = list(dataset)

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

#classRank = []
#for i in range(0, trainLen):
#    if trainData[i][8] not in classRank:
#        classRank.append(trainData[i][8])

#print(classRank)

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

for i in range(0, trainLen):
    s0 = trainData[i][0]
    s1 = trainData[i][1]
    s2 = trainData[i][2]
    s3 = trainData[i][3]
    s4 = trainData[i][4]
    s5 = trainData[i][5]
    s6 = trainData[i][6]
    s7 = trainData[i][7]
    s8 = trainData[i][8]
    distance = []
    classRank = []

    for yy in range(0,trainLen):
        if trainData[yy][8] not in classRank and yy!=i:
            classRank.append(trainData[yy][8])

    for yy in range(0,trainLen):
        distance.append([0] * 2)

    for j in range(0,trainLen):
        if j!=i:
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

        else:
            distance[j][0] = 99999999999999999
            distance[j][1] = trainData[j][8]

    if i == 4:
        print(distance)
    distance.sort(key=lambda x: x[0])

    if i == 4:
        print(distance)

#-----------------------------------------------------  k1 ------------------------------------------------------------------

    k1ClassList = []
    for nv in range(0,k1):
        k1ClassList.append(distance[nv][1])

    print(k1ClassList)


    k1UniqueClassList = []
    k1ClassFrequency = []

    for k in range(0, k1):
        k1ClassFrequency.append(0)

    for k in range(0,k1):
        if(k1ClassList[k] not in k1UniqueClassList):
            k1UniqueClassList.append(k1ClassList[k])

        kk = k1UniqueClassList.index(k1ClassList[k])
        k1ClassFrequency[kk] = k1ClassFrequency[kk] + 1

    print(k1UniqueClassList)
    print(k1ClassFrequency)
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
    print(prediction)
    if (s8 != prediction):
        wrongCount1 = wrongCount1 + 1
        print("Wrong")

#----------------------------------- k1 print --------------------------------------------------------------------------

#-----------------------------------------------------  k2 ------------------------------------------------------------------

    k2ClassList = []
    for nv in range(0,k2):
        k2ClassList.append(distance[nv][1])

    print(k2ClassList)


    k2UniqueClassList = []
    k2ClassFrequency = []

    for k in range(0, k2):
        k2ClassFrequency.append(0)

    for k in range(0,k2):
        if(k2ClassList[k] not in k2UniqueClassList):
            k2UniqueClassList.append(k2ClassList[k])

        kk = k2UniqueClassList.index(k2ClassList[k])
        k2ClassFrequency[kk] = k2ClassFrequency[kk] + 1

    print(k2UniqueClassList)
    print(k2ClassFrequency)
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
    print(prediction)
    if (s8 != prediction):
        wrongCount2 = wrongCount2 + 1
        print("Wrong")

#----------------------------------- k1 print --------------------------------------------------------------------------


#-----------------------------------------------------  k3 ------------------------------------------------------------------

    k3ClassList = []
    for nv in range(0,k3):
        k3ClassList.append(distance[nv][1])

    print(k3ClassList)


    k3UniqueClassList = []
    k3ClassFrequency = []

    for k in range(0, k3):
        k3ClassFrequency.append(0)

    for k in range(0,k3):
        if(k3ClassList[k] not in k3UniqueClassList):
            k3UniqueClassList.append(k3ClassList[k])

        kk = k3UniqueClassList.index(k3ClassList[k])
        k3ClassFrequency[kk] = k3ClassFrequency[kk] + 1

    print(k3UniqueClassList)
    print(k3ClassFrequency)
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
    print(prediction)
    if (s8 != prediction):
        wrongCount3 = wrongCount3 + 1
        print("Wrong")

#----------------------------------- k1 print --------------------------------------------------------------------------

correct1 = trainLen-wrongCount1
correct2 = trainLen-wrongCount2
correct3 = trainLen-wrongCount3

accuracy1 = correct1/trainLen
accuracy2 = correct2/trainLen
accuracy3 = correct3/trainLen

print(wrongCount1)
print(trainLen)
print(trainLen-wrongCount1)
print((trainLen-wrongCount1)/trainLen)


print(wrongCount2)
print(trainLen)
print(trainLen-wrongCount2)
print((trainLen-wrongCount2)/trainLen)


print(wrongCount3)
print(trainLen)
print(trainLen-wrongCount3)
print((trainLen-wrongCount3)/trainLen)


#-----------------------------------------------------------------------------------------------------------------------
if accuracy1 > accuracy2 and accuracy1 > accuracy3:
    kBest = k1

elif accuracy2 > accuracy1 and accuracy2 > accuracy3:
    kBest = k2

elif accuracy3 > accuracy1 and accuracy3 > accuracy2:
    kBest = k3


classRankFinal = []
for i in range(0, trainLen):
    if trainData[i][8] not in classRankFinal:
        classRankFinal.append(trainData[i][8])
print(classRankFinal)



detectedFinal = []


predictionClassList1Final = []

wrongCountFinal = 0

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
    distanceFinal = []

    for yy in range(0,trainLen):
        distanceFinal.append([0] * 2)

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
        resFinal = (s0 - r0) ** 2 + (s1 - r1) ** 2 + (s2 - r2) ** 2 + (s3 - r3) ** 2 + (s4 - r4) ** 2 + ( s5 - r5) ** 2 + (s6 - r6) ** 2 + (s7 - r7) ** 2
        #print(str(j) +"rq " + str(r1))
        resFinal = np.sqrt(resFinal)

        distanceFinal[j][0] = resFinal
        distanceFinal[j][1] = r8

    if i == 4:
        print(distanceFinal)
    distanceFinal.sort(key=lambda x: x[0])
    if i == 4:
        print(distanceFinal)

    k1ClassListFinal = []
    for nv in range(0,kBest):
        k1ClassListFinal.append(distanceFinal[nv][1])

    print(k1ClassListFinal)

    k1UniqueClassListFinal = []
    k1ClassFrequencyFinal = []

    for k in range(0, kBest):
        k1ClassFrequencyFinal.append(0)

    for k in range(0,kBest):
        if(k1ClassListFinal[k] not in k1UniqueClassListFinal):
            k1UniqueClassListFinal.append(k1ClassListFinal[k])

        kk = k1UniqueClassListFinal.index(k1ClassListFinal[k])
        k1ClassFrequencyFinal[kk] = k1ClassFrequencyFinal[kk] + 1

    print(k1UniqueClassListFinal)
    print(k1ClassFrequencyFinal)
    mk = k1ClassFrequencyFinal[0]    #what is the highest frequency
    mkc = 1                     # how many have the highest frequency
    for k in range(1, kBest):
        if k1ClassFrequencyFinal[k] > mk:
            mk = k1ClassFrequencyFinal[k]
            mkc = 1

        elif k1ClassFrequencyFinal[k] == mk:
            mkc = mkc + 1

    if mkc == 1:
        kk = k1ClassFrequencyFinal.index(mk)
        prediction = k1UniqueClassListFinal[kk]
        # predictionClassList1.append(prediction)

    else:
        tempclasscheck = len(classRankFinal) + 1
        for k in range(0, k1):
            if k1ClassFrequencyFinal[k] == mk:
                kkk = classRankFinal.index(k1UniqueClassListFinal[k])
                if tempclasscheck > kkk:
                    tempclasscheck = kkk
                    prediction = classRankFinal[kkk]
        # predictionClassList1.append(prediction)

    predictionClassList1Final.append(prediction)
    if (s8 != prediction):
        wrongCountFinal = wrongCountFinal + 1
        print("Wrong")


print(wrongCountFinal)
print(testLen)
print(testLen-wrongCountFinal)
correctFinal = testLen-wrongCountFinal
accuracyFinal = correctFinal/testLen

#--------------------------------------------------- print ------------------------------------------------------------
print("Number of incorrectly classified instances for k = "+ str(k1)+" : "+str(correct1))
print("Number of incorrectly classified instances for k = "+ str(k2)+" : "+str(correct2))
print("Number of incorrectly classified instances for k = "+ str(k3)+" : "+str(correct3))
print("Best k value : "+str(kBest))
for i in range(0,testLen):
    print("Predicted class : "+predictionClassList1Final[i]	+"  Actual class : "+ testData[i][8])

print("Number of correctly classified instances : "+ str(correctFinal))
print("Total number of instances : "+str(testLen))
print("Accuracy : "+str(accuracyFinal))



