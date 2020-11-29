import arff
import numpy as np
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
print("Enter K1, K2 and K3 : ")
wkt1, wkt2, wkt3 = input('').split()
wk1 = int(wkt1)
wk2 = int(wkt2)
wk3 = int(wkt3)
#print(wk1)
#print(wk2)
#print(wk3)


wresponse1 = []
wresponse2 = []
wresponse3 = []

wWrongCount1 = 0
wWrongCount2 = 0
wWrongCount3 = 0

wk1MAE = 0
wk2MAE = 0
wk3MAE = 0

for i in range(0,wTrainLen):
    ws0 = wTrainData[i][0]
    ws1 = wTrainData[i][1]
    ws2 = wTrainData[i][2]
    ws3 = wTrainData[i][3]
    ws4 = wTrainData[i][4]
    ws5 = wTrainData[i][5]
    ws6 = wTrainData[i][6]
    ws7 = wTrainData[i][7]
    ws8 = wTrainData[i][8]
    ws9 = wTrainData[i][9]
    ws10 = wTrainData[i][10]
    ws11 = wTrainData[i][11]
    #s12 = wTestData[i][12]
    wdistance = []



    for yy in range(0,wTrainLen):
        wdistance.append([0] * 2)

    #print(wdistance)

    for j in range(0,wTrainLen):
        if(j!=i):
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

        else:
            wdistance[j][0] = 9999999999
            wdistance[j][1] = wTrainData[j][11]

    wdistance.sort(key=lambda x: x[0])


#--------------------------------------------------------------------- ki --------------------------------------


    wk1ResponseList = []
    for nv in range(0, wk1):
        wk1ResponseList.append(wdistance[nv][1])

    #print(wk1ResponseList)

    wsumk1RL = sum(wk1ResponseList)
    wavgk1RL = wsumk1RL / wk1
    #print(wavgk1RL)
    wresponse1.append(wavgk1RL)

    if (wavgk1RL != ws11):
        wWrongCount1 = wWrongCount1 + 1
        wk1MAE = wk1MAE + abs(wavgk1RL - ws11)

    #print(wk1MAE / (i + 1))
    #print(i + 1)

# -----------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------- k2 --------------------------------------

    wk2ResponseList = []
    for nv in range(0, wk2):
        wk2ResponseList.append(wdistance[nv][1])

    #print(wk2ResponseList)

    wsumk2RL = sum(wk2ResponseList)
    wavgk2RL = wsumk2RL / wk2
    #print(wavgk2RL)
    wresponse2.append(wavgk2RL)

    if (wavgk2RL != ws11):
        wWrongCount2 = wWrongCount2 + 1
        wk2MAE = wk2MAE + abs(wavgk2RL - ws11)

    #print(wk2MAE / (i + 1))
    #print(i + 1)

# -----------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------- k3 --------------------------------------

    wk3ResponseList = []
    for nv in range(0, wk3):
        wk3ResponseList.append(wdistance[nv][1])

    #print(wk3ResponseList)

    wsumk3RL = sum(wk3ResponseList)
    wavgk3RL = wsumk3RL / wk3
    #print(wavgk3RL)
    wresponse3.append(wavgk3RL)

    if (wavgk3RL != ws11):
        wWrongCount3 = wWrongCount3 + 1
        wk3MAE = wk3MAE + abs(wavgk3RL - ws11)

    #print(wk3MAE / (i + 1))
    #print(i + 1)

# -----------------------------------------------------------------------------------------------------------------------


wk1MAE = wk1MAE / wTrainLen
wk2MAE = wk2MAE / wTrainLen
wk3MAE = wk3MAE / wTrainLen

#print(wk1MAE)
#print(wk2MAE)
#print(wk3MAE)

if wk1MAE<wk2MAE and wk1MAE<wk3MAE:
    wkBest = wk1

elif wk2MAE<wk1MAE and wk2MAE<wk3MAE:
    wkBest = wk2

elif wk3MAE<wk1MAE and wk3MAE<wk2MAE:
    wkBest = wk3


#----------------------------------------------------------

finalwresponse1 = []
finalwWrongCount =0
finalwk1MAE = 0

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
    finalwdistance = []



    for yy in range(0,wTrainLen):
        finalwdistance.append([0] * 2)

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

        finalwres1 = (ws0 - wr0) ** 2 + (ws1 - wr1) ** 2 + (ws2 - wr2) ** 2 + (ws3 - wr3) ** 2 + (ws4 - wr4) ** 2 + (
                    ws5 - wr5) ** 2 + (ws6 - wr6) ** 2 \
                + (ws7 - wr7) ** 2 + (ws8 - wr8) ** 2 + (ws9 - wr9) ** 2 + (ws10 - wr10) ** 2
            # print(str(j) +"rq " + str(r1))
        finalwres1 = np.sqrt(finalwres1)

        # wdistance.append(wres1)
        finalwdistance[j][0] = finalwres1
        finalwdistance[j][1] = wr11
        # if wres1 == 0:
        #   print(j)

    #print(wdistance)
    finalwdistance.sort(key=lambda x: x[0])

    finalwk1ResponseList = []
    for nv in range(0, wkBest):
        finalwk1ResponseList.append(finalwdistance[nv][1])


    #print(finalwk1ResponseList)
    finalwsumk1RL = sum(finalwk1ResponseList)
    finalwavgk1RL = finalwsumk1RL / wkBest
    #print(finalwavgk1RL)
    finalwresponse1.append(finalwavgk1RL)

    if (finalwavgk1RL != ws11):
        finalwWrongCount = finalwWrongCount + 1
        finalwk1MAE = finalwk1MAE + abs(finalwavgk1RL - ws11)

    #print(finalwk1MAE / (i + 1))
    #print(i + 1)

    # -----------------------------------------------------------------------------------------------------------------------

finalwk1MAE = finalwk1MAE / wTestLen
#print(finalwk1MAE)


print("Mean absolute error for k = "+str(wk1)+" : "+str(wk1MAE))
print("Mean absolute error for k = "+str(wk2)+" : "+str(wk2MAE))
print("Mean absolute error for k = "+str(wk3)+" : "+str(wk3MAE))
print("Best k value : " + str(wkBest))
for i in range(0, wTestLen):

    wTestResponse = wTestData[i][11]
    print("Predicted Value : " + str(finalwresponse1[i]) + "    Actual Value : " + str(wTestResponse))

print("Mean absolute error : "+ str(finalwk1MAE))
print("Total number of instances : "+str(wTestLen))




