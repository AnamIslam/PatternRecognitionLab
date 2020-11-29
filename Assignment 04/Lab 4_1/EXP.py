print("The Number of samples, s : ")
s = int(input())
print("The Number of classes, Class : ")
cl = int(input())
print("The number of feature, f : ")
f = int(input())
print("Enter c : ")
c = int(input())
print("Enter k : ")
ka = int(input())

trainSet = []
for i in range(s):
    row = input().split(" ")
    row = list(map(int, row))
    print(row)
    trainSet.append(row)

#functionMatrix = [[0 for i in range(f+1)] for j in range(cl)]
functionMatrix = [
    [0, 0, 0],
    [0, 0, 0],
]
print(functionMatrix)

itr = 0
count = 0
while 1:
    error = False
    for i in range(s):
        values_of_D = []
        actualClass = trainSet[i][f]
        for j in range(cl):
            D = 0
            for k in range(f+1):
                if k == 0:
                    D = D + functionMatrix[j][k]
                else:
                    D =  D + functionMatrix[j][k]*trainSet[i][k-1]
            values_of_D.append([D, j])
        values_of_D.sort(key=lambda x: x[0], reverse=True)  # f is the index of class
        # i is the index of the train samples
        class_prdicted = values_of_D[0][1]
        itr = itr + 1
        if actualClass == class_prdicted:
            count = count + 1
            print(i, "no error count",count)
            if count == s:
                break
        else:
            error = True
            count = 0
            print(i, "no error count", count)
            for k in range(f+1):
                if k == 0:
                    functionMatrix[actualClass][k] = functionMatrix[actualClass][k] + (c * 1 * ka)
                else:
                    functionMatrix[actualClass][k] = functionMatrix[actualClass][k] + (c * 1 * trainSet[i][k-1])
            for k in range(f+1):
                if k == 0:
                    functionMatrix[class_prdicted][k] = functionMatrix[class_prdicted][k] - (c * 1 * ka)
                else:
                    functionMatrix[class_prdicted][k] = functionMatrix[class_prdicted][k] - (c * 1 * trainSet[i][k-1])

    #print(error)
    if not error:
        break

for i in range(cl):
    print("D"+str(i))
    for j in range(f+1):
        print(functionMatrix[i][j], end=" ")
    print("")
# print(functionMatrix)
#print(itr,"iteration")