import numpy as np

print("Enter Number of sample")
numS = int(input())

print("Enter number of features")
numF = int(input())

print("Enter K")
k = int(input())

sampleList = []

for i in range(0,numS):
    sampleList.append([int(0) for j in range(0,numF)])

for i in range(0,numS):
    x = input()
    xlist = x.split()
    print(xlist)
    for j in range(0,numF):
        sampleList[i][j] = int(xlist[j])

print(sampleList)

initialCent = []
for i in range(0,k):
    initialCent.append(sampleList[i])

print(initialCent)

flag = 0
while 1<2:
    #print("sample list check 6")
    #print(sampleList)
    centSelect = []
    for i in range(0, numS):
        #print("present sample")
        #print(sampleList[i])
        distance = []
        for j in range(0, k):
            tempdis = 0
            for j2 in range(0, numF):
                tempdis = tempdis + (sampleList[i][j2] - initialCent[j][j2]) ** 2
            tempdis = np.sqrt(tempdis)
            distance.append(tempdis)
        #print("distance List")
        #print(distance)
        minDis = min(distance)
        #print("Minimum distance")
        #print(minDis)
        mdi = distance.index(minDis)
        #print("Index of minimum distance")
        #print(mdi)
        centSelect.append(mdi)
    #print("centroid selected")
    #print(centSelect)
    #print("sample list check")
    #print(sampleList)

    # sum of centroid elements
    stc = []
    for i in range(0, k):
        stc.append([int(0) for j in range(0, numF)])

    #print("sample list check 2")
    #print(sampleList)

    cenFreq = []
    for i in range(0, k):
        cenFreq.append(0)

    #print("sample list check 3")
    #print(sampleList)

    for i in range(0, numS):
        indx = centSelect[i]
        cenFreq[indx] = cenFreq[indx] + 1
        for j in range(0, numF):
            stc[indx][j] = stc[indx][j] + sampleList[i][j]

    #print("sample list check 4")
    #print(sampleList)

    #print("Sum of sample in centroids")
    #print(stc)
    #print("centroid frequency")
    #print(cenFreq)

    for i in range(0, k):
        #print("Centfreq[i]" + str(cenFreq[i]))
        for j in range(0, numF):
            stc[i][j] = stc[i][j] / cenFreq[i]

    #print("sample list check 5")
    #print(sampleList)

    #print("Updated centroids")
    #print(stc)
    #print("sample list check 8")
    #print(sampleList)
    if (initialCent == stc):
        print("Milegeche")
        flag = 1
        print("Final centroid")
        print(initialCent)
        break

    else:
        print("hoi ni")
        initialCent = []
        for i in range(0, k):
            initialCent.append([int(0) for j in range(0, numF)])
        for i in range(0, k):
            for j in range(0, numF):
                #print("Initial " + str(initialCent[i][j]))
                #print("stc " + str(stc[i][j]))
                #print("samplelist1" + str(sampleList[i][j]))
                initialCent[i][j] = stc[i][j]
                #print("samplelist2" + str(sampleList[i][j]))
                #print("stc")
                #print(stc)

                #print("sample list check in vitrer loop")
                #print(sampleList)
            #print("sample list check in loop")
            #print(sampleList)

    #print("sample list check 7")
    #print(sampleList)
    print("-----------------")
    print(initialCent)



