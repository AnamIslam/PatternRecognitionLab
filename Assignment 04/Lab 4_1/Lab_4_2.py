#Number of class
print("Enter The Number of sample")
numS = int(input())
print(numS)

print("Enter The Number of classes")
numC = int(input())
print(numC)


#Number of features in each sample
print("Enter the number of features in each sample")
numFi = int(input())

#c
print("Enter c")
c = int(input())

#k
print("Enter k")
k = int(input())

numF = numFi+1
#weight initialization
wi = []

for i in range(0,numC):
    wi.append([int(i+j) for j in range(0,numF)])

print(wi)

eqList = []

for i in range(0,numS):
    eqList.append([int(1) for j in range(0,numF)])

print(eqList)

d = []
for i in range(0,numS):
    x = input()
    xlist = x.split()
    print(xlist)
    for j in range(1,numF):
        print(xlist[j-1])
        eqList[i][j] = int(xlist[j-1])
    d.append(int(xlist[numF-1]))

print(eqList)
print(d)

flag = 0
final = 0

while 1<2:   #------------------------------------ outer loop for flag check
    for i in range(0,numS):     #----------------- sample loop
        reslist = []
        for j in range(0,numC):    #-------------- equation loop

            tempres = 0
            print("j " + str(j))
            for jj in range(0,numF):
                tempres = tempres + wi[j][jj] * eqList[i][jj]

            #print("tempres"+str(tempres))
            reslist.append(tempres)
            print(reslist)

        maxval = max(reslist)
        print(maxval)
        tempd = d[i]

        print(tempd)
        #print(reslist)
        print(reslist[tempd])
        if(maxval != reslist[tempd]):
            flag = 0
            maxvalindx = reslist.index(maxval)
            print(maxvalindx)
            print("wold not class")
            print(wi[maxvalindx])

            wi[maxvalindx][0] = wi[maxvalindx][0] - c * k
            for jj in range(1, numF):
                wi[maxvalindx][jj] = wi[maxvalindx][jj]-c*eqList[maxvalindx][jj]

            print("wnew not class")
            print(wi[maxvalindx])


            targetIndex = d[i]
            print("Wold real")
            print(wi[targetIndex])
            wi[targetIndex][0] = wi[targetIndex][0] + c * k
            for jj in range(1,numF):
                wi[targetIndex][jj] = wi[targetIndex][jj] + c * eqList[targetIndex][jj]
            print("Wnew real")
            print(wi[targetIndex])

        else:
            flag = flag+1
            print("---------------------------")
            print(flag)
            if flag == numS:
                final = 1
                break

    if(final == 1):
        break




print(wi)








