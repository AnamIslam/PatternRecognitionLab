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

classRank = []
for i in range(0, trainLen):
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

    tempTrainList = []

    for j in range(0, trainLen):
        if (j != i):
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

        else:
            distance.append(999999)

#----------------------------------------------------------------------- k1 --------------------------------------------

    k1List = nsmallest(k1,distance)
    print(k1List)
    k1ClassList = []

    for k in range(0,k1):
        kk = distance.index(k1List[k])
        k1ClassList.append(trainData[kk][8])

    print(k1ClassList)

    k1UniqueClassList = []
    k1ClassFrequency = []

    for k in range(0,k1):
        k1ClassFrequency.append(0)

    for k in range(0,k1):
        if(k1ClassList[k] not in k1UniqueClassList):
            k1UniqueClassList.append(k1ClassList[k])

        kk = k1UniqueClassList.index(k1ClassList[k])
        k1ClassFrequency[kk] = k1ClassFrequency[kk] + 1



    print(k1UniqueClassList)
    print(k1ClassFrequency)
    mk = k1ClassFrequency[0]
    mkc = 1
    for k in range(1,k1):
        if k1ClassFrequency[k]>mk:
            mk = k1ClassFrequency[k]
            mkc = 1

        elif k1ClassFrequency[k]==mk:
            mkc = mkc+1



    if mkc==1:
        kk = k1ClassFrequency.index(mk)
        prediction = k1UniqueClassList[kk]
        #predictionClassList1.append(prediction)

    else:
        tempclasscheck = len(classRank)+1
        for k in range(0,k1):
            if k1ClassFrequency[k] == mk:
                kkk = classRank.index(k1UniqueClassList[k])
                if tempclasscheck > kkk:
                    tempclasscheck = kkk
                    prediction = classRank[kkk]
        #predictionClassList1.append(prediction)





    predictionClassList1.append(prediction)
    if(s8 != prediction):
        wrongCount1 = wrongCount1+1
        print("Wrong")



#-----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------- k2 --------------------------------------------

    k2List = nsmallest(k2, distance)
    print(k2List)
    k2ClassList = []

    for k in range(0, k2):
        kk = distance.index(k2List[k])
        k2ClassList.append(trainData[kk][8])

    print(k2ClassList)

    k2UniqueClassList = []
    k2ClassFrequency = []

    for k in range(0, k2):
        k2ClassFrequency.append(0)

    for k in range(0, k2):
        if (k2ClassList[k] not in k2UniqueClassList):
            k2UniqueClassList.append(k2ClassList[k])

        kk = k2UniqueClassList.index(k2ClassList[k])
        k2ClassFrequency[kk] = k2ClassFrequency[kk] + 1

    print(k2UniqueClassList)
    print(k2ClassFrequency)
    mk = k2ClassFrequency[0]
    mkc = 1
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
        print("Wrong")

#-----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------- k3 --------------------------------------------

    k3List = nsmallest(k3, distance)
    print(k3List)
    k3ClassList = []

    for k in range(0, k3):
        kk = distance.index(k3List[k])
        k3ClassList.append(trainData[kk][8])

    print(k3ClassList)

    k3UniqueClassList = []
    k3ClassFrequency = []

    for k in range(0, k3):
        k3ClassFrequency.append(0)

    for k in range(0, k3):
        if (k3ClassList[k] not in k3UniqueClassList):
            k3UniqueClassList.append(k3ClassList[k])

        kk = k3UniqueClassList.index(k3ClassList[k])
        k3ClassFrequency[kk] = k3ClassFrequency[kk] + 1

    print(k3UniqueClassList)
    print(k3ClassFrequency)
    mk = k3ClassFrequency[0]
    mkc = 1
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
        print(prediction +" Wrong")

#-----------------------------------------------------------------------------------------------------------------------

print(wrongCount1)
print(wrongCount2)
print(wrongCount3)
print(i)

if wrongCount1< wrongCount2 and wrongCount1<wrongCount3:
    kBest = k1
elif wrongCount2<wrongCount1 and wrongCount2<wrongCount3:
    kBest = k2
elif wrongCount3<wrongCount1 and wrongCount3<wrongCount2:
    kBest = k3



#-------------------------------------------------------------------------- Final ----------------------------------------

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

        distanceFinal.append(resFinal)
#----------------------------------------------------------------------- k1 --------------------------------------------



    k1ListFinal = nsmallest(kBest,distanceFinal)
    print(k1ListFinal)
    k1ClassListFinal = []

    for k in range(0,kBest):
        kk = distanceFinal.index(k1ListFinal[k])
        k1ClassListFinal.append(trainData[kk][8])

    print(k1ClassListFinal)

    k1UniqueClassListFinal = []
    k1ClassFrequencyFinal = []

    for k in range(0,kBest):
        k1ClassFrequencyFinal.append(0)

    for k in range(0,kBest):
        if(k1ClassListFinal[k] not in k1UniqueClassListFinal):
            k1UniqueClassListFinal.append(k1ClassListFinal[k])

        kk = k1UniqueClassListFinal.index(k1ClassListFinal[k])
        k1ClassFrequencyFinal[kk] = k1ClassFrequencyFinal[kk] + 1



    print(k1UniqueClassListFinal)
    print(k1ClassFrequencyFinal)
    mkFinal = k1ClassFrequencyFinal[0] #what is the highest frequency
    mkcFinal = 1  # how many have the highest frequency


    #if frequency are same
    for k in range(1,kBest):
        if k1ClassFrequencyFinal[k]>mkFinal:
            mkFinal = k1ClassFrequencyFinal[k]
            mkcFinal = 1

        elif k1ClassFrequencyFinal[k]==mkFinal:
            mkcFinal = mkcFinal+1



    if mkcFinal==1:
        kk = k1ClassFrequencyFinal.index(mkFinal)
        predictionFinal = k1UniqueClassListFinal[kk]
        #predictionClassList1.append(prediction)

    else:
        tempclasscheckFinal = len(classRank)+1
        for k in range(0,kBest):
            if k1ClassFrequencyFinal[k] == mkFinal:
                kkk = classRank.index(k1UniqueClassListFinal[k])
                if tempclasscheckFinal > kkk:
                    tempclasscheckFinal = kkk
                    predictionFinal = classRank[kkk]
        #predictionClassList1.append(prediction)





    predictionClassList1Final.append(predictionFinal)
    if(s8 != predictionFinal):
        wrongCountFinal = wrongCountFinal+1
        print("Wrong")
    print(wrongCountFinal)
    print(i)

correctFinal = testLen - wrongCountFinal
accuracyFinal = correctFinal/testLen
print("Number of incorrectly classified instances for k =" + str(k1)+" : "+str(wrongCount1))
print("Number of incorrectly classified instances for k =" + str(k2)+" : "+str(wrongCount2))
print("Number of incorrectly classified instances for k =" + str(k3)+" : "+str(wrongCount3))
print("Best k value : "+str(kBest))
for i in range(0, testLen):
    testcls = testData[i][8]
    print("Predicted Class : " + str(predictionClassList1Final[i]) + "    Actual Class : " + str(testcls))

print("Number of correctly classified instances : " + str(correctFinal))
print("Total number of instances : "+ str(testLen))
print("Accuracy : " + str(accuracyFinal))


