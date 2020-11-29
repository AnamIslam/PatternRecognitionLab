#number of train data
n = 7
k = 3

trainSet = [[4, 4], [8, 4], [15, 8], [20, 6], [21, 10],[24, 4], [24, 12]]

centroid = []
centroid.append(trainSet[0])
centroid.append(trainSet[2])
centroid.append(trainSet[4])

#t = 2
#while t:
temp = []
results_temp = [0 for i in range(k)]
print("result Temp")
print(results_temp)
for i in range(n):
    sample = trainSet[i]
    mini = 10000
    index = 0
    for j in range(k):
        cd = abs(sample[0] - centroid[j][0]) + abs(sample[1] - centroid[j][1])
        if cd < mini:
            mini = cd
            index = j
            results_temp[j] += 1
    temp.append([i, index])

    for j in range(k):
        sumx = 0
        sumy = 0
        num = 0
        for p in range(len(temp)):
            if temp[p][1] == j:
                sumx += trainSet[p][0]
                sumy += trainSet[p][1]
                num += 1
        if num > 0:
            x = sumx / num
            y = sumy / num
            centroid[j] = [x, y]
    print("Sample")
    print(trainSet[i])
    print("Selected centroid")
    print(index)
    print("Centroid")
    print(centroid)
