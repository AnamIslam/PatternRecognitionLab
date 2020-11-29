import arff
import numpy as np
import matplotlib.pyplot as plt
from heapq import nsmallest


wTrainDataset = arff.load(open('wine_train.arff', 'rb'))
#data = np.array(dataset['data'])
#allData = list(dataset)

#print(wTrainDataset)
wTrainData = list(arff.load('wine_train.arff'))
wTrainLen = len(wTrainData)
#print(wTrainData)
#print(wTrainLen)

wTestDataset = arff.load(open('wine_test.arff', 'rb'))
wTestData = list(arff.load('wine_test.arff'))
wTestLen = len(wTestData)
#print(wTestData)
#print(wTestLen)

#print(wTestData[0][11])

#wkt1, wkt2, wkt3 = input('').split()
#wkt1= input('')

wk1 = 1
wk2 = 2
wk3 = 3
wk4 = 5
wk5 = 10
#wk2 = int(wkt2)
#wk3 = int(wkt3)
#print(wk1)
#print(wk2)
#print(wk3)


wresponse1 = []
wresponse2 = []
wresponse3 = []
wresponse4 = []
wresponse5 = []

wWrongCount1 = 0
wWrongCount2 = 0
wWrongCount3 = 0
wWrongCount4 = 0
wWrongCount5 = 0

wk1MAE = 0
wk2MAE = 0
wk3MAE = 0
wk4MAE = 0
wk5MAE = 0

for i in range(0,wTestLen):
    ws0 = wTestData[i][0]
    ws1 = wTestData[i][1]
    ws2 = wTestData[i][2]
    ws3 = wTestData[i][3]
    ws4 = wTestData[i][4]
    ws5 = wTestData[i][5]
    ws6 = wTestData[i][6]
    ws7 = wTestData[i][7]
    ws8 = wTestData[i][8]
    ws9 = wTestData[i][9]
    ws10 = wTestData[i][10]
    ws11 = wTestData[i][11]
    #s12 = wTestData[i][12]
    wdistance = []



    for yy in range(0,wTrainLen):
        wdistance.append([0] * 2)

    #print(wdistance)

    for j in range(0,wTrainLen):
        wr0 = wTrainData[j][0]
        wr1 = wTrainData[j][1]
        wr2 = wTrainData[j][2]
        wr3 = wTrainData[j][3]
        wr4 = wTrainData[j][4]
        wr5 = wTrainData[j][5]
        wr6 = wTrainData[j][6]
        wr7 = wTrainData[j][7]
        wr8 = wTrainData[j][8]
        wr9 = wTrainData[j][9]
        wr10 = wTrainData[j][10]
        wr11 = wTrainData[j][11]
            # wr12 = wTrainData[j][12]

        wres1 = (ws0 - wr0) ** 2 + (ws1 - wr1) ** 2 + (ws2 - wr2) ** 2 + (ws3 - wr3) ** 2 + (ws4 - wr4) ** 2 + (
                    ws5 - wr5) ** 2 + (ws6 - wr6) ** 2 \
                + (ws7 - wr7) ** 2 + (ws8 - wr8) ** 2 + (ws9 - wr9) ** 2 + (ws10 - wr10) ** 2
            # print(str(j) +"rq " + str(r1))
        wres1 = np.sqrt(wres1)

            #wdistance.append(wres1)
        wdistance[j][0] = wres1
        wdistance[j][1] = wr11
        #if wres1 == 0:
         #   print(j)


    #print(wdistance)
    wdistance.sort(key=lambda x : x[0])


#------------------------------------------------------------- k1 ------------------------------------------------------
    wk1ResponseList = []
    for nv in range(0,wk1):
        wk1ResponseList.append(wdistance[nv][1])

    #print(wk1ResponseList)

    wsumk1RL = sum(wk1ResponseList)
    wavgk1RL = wsumk1RL / wk1
    #print(wavgk1RL)
    wresponse1.append(wavgk1RL)

    if (wavgk1RL != ws11):
        wWrongCount1 = wWrongCount1 + 1
        wk1MAE = wk1MAE + abs(wavgk1RL - ws11)

    #print(wk1MAE/(i+1))
    #print(i+1)
# -----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------- k2 ------------------------------------------------------

    wk2ResponseList = []
    for nv in range(0,wk2):
        wk2ResponseList.append(wdistance[nv][1])

    #print(wk1ResponseList)

    wsumk2RL = sum(wk2ResponseList)
    wavgk2RL = wsumk2RL / wk2
    #print(wavgk1RL)
    wresponse2.append(wavgk2RL)

    if (wavgk2RL != ws11):
        wWrongCount2 = wWrongCount2 + 1
        wk2MAE = wk2MAE + abs(wavgk2RL - ws11)

    #print(wk1MAE/(i+1))
    #print(i+1)
# -----------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------- k3 ------------------------------------------------------

    wk3ResponseList = []
    for nv in range(0, wk3):
        wk3ResponseList.append(wdistance[nv][1])

    # print(wk1ResponseList)

    wsumk3RL = sum(wk3ResponseList)
    wavgk3RL = wsumk3RL / wk3
    # print(wavgk1RL)
    wresponse3.append(wavgk3RL)

    if (wavgk3RL != ws11):
        wWrongCount3 = wWrongCount3 + 1
        wk3MAE = wk3MAE + abs(wavgk3RL - ws11)

    # print(wk1MAE/(i+1))
    # print(i+1)
# -----------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------- k4 ------------------------------------------------------

    wk4ResponseList = []
    for nv in range(0, wk4):
        wk4ResponseList.append(wdistance[nv][1])

    # print(wk1ResponseList)

    wsumk4RL = sum(wk4ResponseList)
    wavgk4RL = wsumk4RL / wk4
    # print(wavgk1RL)
    wresponse4.append(wavgk4RL)

    if (wavgk4RL != ws11):
        wWrongCount4 = wWrongCount4 + 1
        wk4MAE = wk4MAE + abs(wavgk4RL - ws11)

    # print(wk1MAE/(i+1))
    # print(i+1)
# -----------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------- k5 ------------------------------------------------------

    wk5ResponseList = []
    for nv in range(0, wk5):
        wk5ResponseList.append(wdistance[nv][1])

    # print(wk1ResponseList)

    wsumk5RL = sum(wk5ResponseList)
    wavgk5RL = wsumk5RL / wk5
    # print(wavgk1RL)
    wresponse5.append(wavgk5RL)

    if (wavgk5RL != ws11):
        wWrongCount5 = wWrongCount5 + 1
        wk5MAE = wk5MAE + abs(wavgk5RL - ws11)

    # print(wk1MAE/(i+1))
    # print(i+1)
# -----------------------------------------------------------------------------------------------------------------------




wk1MAE = wk1MAE / wTestLen
wk2MAE = wk2MAE / wTestLen
wk3MAE = wk3MAE / wTestLen
wk4MAE = wk4MAE / wTestLen
wk5MAE = wk5MAE / wTestLen
#print(wk1MAE)

xAxis = []
yAxis = []

xAxis.append(wk1)
xAxis.append(wk2)
xAxis.append(wk3)
xAxis.append(wk4)
xAxis.append(wk5)

yAxis.append(wk1MAE)
yAxis.append(wk2MAE)
yAxis.append(wk3MAE)
yAxis.append(wk4MAE)
yAxis.append(wk5MAE)


plt.plot(xAxis,yAxis)
plt.xlabel("K Values")
plt.ylabel("Mean Absolute Error")
plt.show()