import numpy as np

print("Enter Number of Train Data : ")
inpt = input()

n = int(inpt)


weight = []
height = []
label = []
bmi =[]

FlagBmiLow=0
FlagBmiHigh=0

print("Enter Train Data : \n")


for i in range(n):
    w1,h1,l1 = input().split()
    weight.append(int(w1))
    height.append(int(h1))
    label.append(l1)
    bmi.append(weight[i]/height[i]**2)


#print(weight)
#print(height)
#print(bmi)


print("Enter Test Data : ")
tw, th = input().split()
testWeight = int(tw)
testHeight =int(th)
testBmi = testWeight/testHeight**2


w = weight[0]
h = height[0]
l = label[0]


#euclidian
simResult = np.sqrt((w - testWeight)**2 + (h - testHeight)**2)
minSim = simResult
classify = l


for i in range(1,n):
    w = weight[i]
    h = height[i]
    l = label[i]
    #euclidian
    simResult = np.sqrt((w - testWeight) ** 2 + (h - testHeight) ** 2)
    if (minSim>simResult):
        minSim = simResult
        classify = l


print(classify)