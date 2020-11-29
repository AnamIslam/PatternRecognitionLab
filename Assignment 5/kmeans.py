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
print("id samplelist", id(sampleList))
sampleList2 = sampleList[:]
print("sampleList2 ---------------------------------------------------")
print(sampleList2)
print("id samplelist2", id(sampleList2))

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
    sampleListlala = sampleList[lala][:]
    print("-----------------------------------print sam[lala]" , id(sampleList[lala]))
    print("-----------------------------------print samlala", id(sampleListlala))
    initialCent.append(sampleListlala)
    print("-----------------------------------print initialCent", id(initialCent[i]))

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

        print("sampleList check")
        print(sampleList)
        tempsamplelist = sampleList[i]

        print("old")
        print(initialCent)
        print(numF)
        for j in range(0,numF):
            print('haha')
            tempsample = tempsamplelist[j][:]
            tempiniCent = int(initialCent[mdi][j])
            tempinitialCent = tempiniCent * (centFreq[mdi]-1) + tempsample
            initialCent[mdi][j] = tempinitialCent/ centFreq[mdi]
        print("updated")
        print(initialCent)
        #print("sampleList check 2")
        #print(sampleList)

#print(centFreq)

'''upDis = []

for i in range(0,numS):
    upDis.append([int(0) for j in range(0,k)])

print(upDis)
print(sampleList2)
print(id(sampleList2))
for i in range(0,numS):
    print(sampleList[i])
    for j in range(0,k):
        print(initialCent[j])
        tempdis = 0
        for j2 in range(0,numF):
            tempdis = tempdis + (sampleList[i][j2] - initialCent[j][j2]) ** 2
            print("Loop er vitre", tempdis)

        tempdis = np.sqrt(tempdis)
        print(tempdis)
        upDis[i][j] = tempdis

print(upDis)
'''