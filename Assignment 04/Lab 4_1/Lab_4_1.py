#Number of sample
print("Enter The Number of sample")
numS = int(input())
print(numS)

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

for i in range(0,numF):
    wi.append(0)

print(wi)
#equation list

eqList = []

for i in range(0,numS):
    eqList.append([int(0) for j in range(0,numF)])

print(eqList)

d = []
for i in range(0,numS):
    x = input()
    xlist = x.split()
    eqList[i][0] = 1
    for j in range(1,numF):
        eqList[i][j] = int(xlist[j-1])
    d.append(int(xlist[numF-1]))

print(eqList)
print(d)

km=0
flag = 0
ps = 0
while 1<2:
    ps = ps+1
    for i in range(0,numS):
        r = 0
        for j in range(0,numF):
            r = r+wi[j]*eqList[i][j]

        km=km+1
        #if km==20:
         #   break
        print("iteration = "+ str(km))
        #print("R = "+str(r))
        if (r>=0 and d[i]>=0) or (r<0 and d[i]<0):
            flag = flag+1
            print("Equation")
            print(eqList[i])
            print("Weight")
            print(wi)
            print("Flag")
            print(flag)
            if flag == numS:
                #print("Break howar kotha")
                break

        else:
            flag = 0
            #print("w[0] : "+ str(wi[0])+" c = "+str(c)+" d[i] : "+str(d[i])+"  k : "+ str(k))
            wi[0] = wi[0]+c*d[i]*k

            for j in range(1,numF):
                wi[j] = wi[j]+c*d[i]*eqList[i][j]

            print("Equation")
            print(eqList[i])
            print("Weight")
            print(wi)
            print("Flag")
            print(flag)

    #if km == 20:
     #   break

    if flag == numS:
        break


print("Iteration = "+ str(km))
print("Pass = "+ str(ps))
print("Final Weight :")
for i in range(0,numF):
    print("w"+str(i)+" = "+str(wi[i]))


