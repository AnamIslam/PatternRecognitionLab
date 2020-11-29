import numpy as np
from scipy.spatial import distance
from tabulate import tabulate


def get_indexes_to_be_merged(entireList):
    List_with_only_values = []

    for row in entireList[1:]:

        value_list_row = []

        for eachValue in row[1:]:
            value_list_row.append(eachValue)

        List_with_only_values.append(value_list_row)

    # print(List_with_only_values)

    np_array = np.array(List_with_only_values)

    # print(np_array)

    min_value = np.min(np_array[np.nonzero(np_array)])

    # print("Min Value is {}".format(min_value))

    result = np.where(np_array == min_value)

    # print(result[0][0])
    # print(result[1][0])

    # print("The Position is {}".format(np.where(np_array == min_value)))

    return [result[0][0], result[1][0]]


def eucledian_distance(point1, point2):
    dst = distance.euclidean(point1, point2)

    return dst


def get_max_distance(list1, list2, indexList):
    if set(list1) == set(list2):

        # return math.nan
        return int(0)


    else:
        # print("Lists are not same ")

        max_distance = 0

        for class1 in list1:

            for class2 in list2:

                distance_calculated = eucledian_distance(indexList[class1 - 1], indexList[class2 - 1])

                if max_distance < distance_calculated:
                    max_distance = distance_calculated

        # print("Minimum Distance is {}".format(min_distance))

        return max_distance


def get_init_matrix(sample, classList):
    # first row
    headerList = [' ']
    for eachClass in classList:
        headerList.append(eachClass)

    # first row
    BroaderList = [headerList]

    for i in range(len(classList)):
        row = [classList[i]]

        for j in classList:
            distance_calculated = get_max_distance(classList[i], j, sample)

            row.append(distance_calculated)

        BroaderList.append(row)

    print(tabulate(BroaderList[1:], headers=BroaderList[0], tablefmt='grid'))

    r, c = get_indexes_to_be_merged(BroaderList)

    # print("r is {} and c is {} ".format(r+1,c+1))

    return [r, c]

    pass


print("Enter Number of sample")
numS = int(input())

print("Enter number of features")
numF = int(input())

sampleList = []

for i in range(0, numS):
    sampleList.append([int(0) for j in range(0, numF)])

print("Enter sample")
for i in range(0, numS):
    x = input()
    xlist = x.split()
    print(xlist)
    for j in range(0, numF):
        sampleList[i][j] = int(xlist[j])

print(sampleList)

# header = [[1], [2], [3], [4], [5]]

header = []
for i in range(0, numS):
    header.append([int(i + 1) for j in range(0, 1)])
print(header)

while (len(header) > 1):

    r, c = get_init_matrix(sampleList, header)

    new_header = []
    merged_list = header[r] + header[c]
    new_list = [merged_list]

    for i in range(len(header)):
        if (not (i == r or i == c)):
            new_list.append(header[i])

    header = new_list

    pass

print("Output : {}".format(header[0]))