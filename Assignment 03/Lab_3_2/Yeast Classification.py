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



#q =trainData[0][0]
#print(q)
k = input('')
k1 = int(k)

print(k1)

print(trainData[445])



detected1 = []


predictionClassList1 = []

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
    distance = []



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

        distance.append(res1)
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


#----------------------------------- k1 print --------------------------------------------------------------------------



print(len(predictionClassList1))
print("For k = "+ str(k1))


for i in range(0,testLen):
    testcls = testData[i][8]
    print("Predicted Class : " + str(predictionClassList1[i])+ "    Actual Class : " + str(testcls))




print(wrongCount1)
correct1 = testLen-wrongCount1
accuracy1 = correct1/testLen
print("Number of Correct : " + str(correct1))
print("Total number of instance : "+str(testLen))
print("Accuracy : " + str(accuracy1))


#-----------------------------------------------------------------------------------------------------------------------



