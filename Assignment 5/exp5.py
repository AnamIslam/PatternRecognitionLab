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

centSelect = []
for i in range(0, numS):
     distance = []
     for j in range(0, k):
          tempdis = 0
          for j2 in range(0, numF):
               tempdis = tempdis + (sampleList[i][j2] - initialCent[j][j2]) ** 2
          tempdis = np.sqrt(tempdis)
          distance.append(tempdis)
     print(distance)
     minDis = min(distance)
     print(minDis)
     mdi = distance.index(minDis)
     print(mdi)
     centSelect.append(mdi)
print(centSelect)


#sum of centroid elements
stc = []
for i in range(0,k):
    stc.append([int(0) for j in range(0,numF)])

cenFreq = []
for i in range(0,k):
     cenFreq.append(0)

for i in range(0,numS):
     indx = centSelect[i]
     cenFreq[indx] = cenFreq[indx]+1
     for j in range(0,numF):
          stc[indx][j] = stc[indx][j] + sampleList[i][j]

print(stc)
print(cenFreq)

for i in range(0,k):
     print("Centfreq[i]" + str(cenFreq[i]))
     for j in range(0,numF):

          stc[i][j] = stc[i][j] / cenFreq[i]


print(stc)
if(initialCent == stc):
     print("Milegeche")

else:
     print("hoi ni")
     for i in range(0,k):
          for j in range(0,numF):
               initialCent[i][j] = stc[i][j]

print(initialCent)
