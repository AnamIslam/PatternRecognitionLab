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

print("Enter sample")
for i in range(0,numS):
    x = input()
    xlist = x.split()
    print(xlist)
    for j in range(0,numF):
        sampleList[i][j] = int(xlist[j])

print(sampleList)

print("Enter centroid samples")
incen = input()
incList = incen.split()
print(incList)
incl = []
for i in range(0,k):
    incl.append(int(incList[i])-1)

print(incl)

initialCent = []
for i in range(0,k):
    lala = incl[i]
    print(lala)
    initialCent.append(sampleList[lala])

print(initialCent)

centFreq = []
for i in range(0,k):
    centFreq.append(1)


for i in range(0, numS):
    distance = []
    print("present sample")
    print(sampleList[i])
    if i not in incl:
        for j in range(0, k):
            tempdis = 0
            print("initial cen")
            print(initialCent)
            print(sampleList[i])
            for j2 in range(0, numF):
                print(sampleList[i][j2])
                print(initialCent[j][j2])
                tempdis = tempdis + (sampleList[i][j2] - initialCent[j][j2]) ** 2
            tempdis = np.sqrt(tempdis)
            print("Tempdis" + str(tempdis))
            distance.append(tempdis)
        print(distance)
        minDis = min(distance)
        print(minDis)
        mdi = distance.index(minDis)
        print(mdi)
        centFreq[mdi] = centFreq[mdi] + 1

        print("old")
        print(initialCent)

        for j in range(0,numF):
            initialCent[mdi][j] = initialCent[mdi][j] * (centFreq[mdi]-1) + sampleList[i][j]
            initialCent[mdi][j] = initialCent[mdi][j]/ centFreq[mdi]
        print("updated")
        print(initialCent)

print(centFreq)
