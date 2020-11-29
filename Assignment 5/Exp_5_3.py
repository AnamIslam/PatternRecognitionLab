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
    incl.append(int(incList[i]))

print(incl)

initialCent = []
for i in range(0,k):
    initialCent.append(incl[i])

print(initialCent)

while 1<2: