import os
import re
import math

print(os.getcwd())

stopList = []

#--------------------------------stop work read and make list of stopwords------------------------------
with open('stopwords.txt','r') as g:
    for line in g:
        for word in line.split():
           stopList.append(word)
           #print(word)
#print("stopList")
#print(stopList)

#------------------------------------------------------------------------------------------------------------------------

#---------------------------------corpus text read------------------------------------

with open("corpus.txt") as f1:
    lines = f1.read()


#--------------------------------- spliting by paragraph---------------------------------

person = lines.split("\n\n")
pperson = len(person)
#print(person)
#print(len(person))
for lenperson in range(0,pperson):
    tempPerson = person[lenperson]
    tempPerson = tempPerson.strip()
    #print(tempPerson)

    person[lenperson]=tempPerson

#print("---------")
#print("Person all in Lower case")
#print(person)
#--------------------------------------------------------------------------------------------

n = int(input())
#print(n)


#---------------------------------------------Spilitting Name,Class,Description---------------------------------------------
classList = []
allclassList = []
allnameList = []
alldesList = []

for i in range(0,n):
    tempName = person[i].split('\n', 2)[0]                      #---Spliting the names
    tempClass = person[i].split('\n', 2)[1]                     #--- Spliting the ClassNAmes
    tempClass = tempClass.rstrip(' ')
    tempDes = person[i].split('\n', 2)[2]                       #---Spliting the descriptions
    allclassList.append(tempClass)
    allnameList.append(tempName)
    alldesList.append(tempDes.lower())
    TCLen = len(tempClass)                                      #---------make a class list
    #print(tempClass)
    #print(TCLen)
    #if tempClass[TCLen]==' ':
    #    tempClass = tempClass[:-1]
    #allclassList.append(tempClass)
    if tempClass not in classList:
        classList.append(tempClass)

#print("Class List")
#print(classList)
#print("All Class List")
#print(allclassList)
#print("All Name List")
#print(allnameList)
#print("All Description List")
#print(alldesList)
#--------------------------------------------------------------------------------------

#in final work classLen wouyld be given by input
classLen = len(classList)                                       #---------- ClassLen is needed to count class frequency

classFreq = []
for i in range(0,classLen):
    classFreq.append(0)

#-----------------------------------Class frequency-------------------------------------
lenAllclassList = len(allclassList)
for ics in range(0,len(allclassList)):
    checkfreq = allclassList[ics]
    temp2 = classList.index(checkfreq)
    classFreq[temp2] = classFreq[temp2] + 1

#print(classList)
#print(classFreq)


#-------------------------------------probability Class-------------------------------------------
#-------------------------------------log probability Class-------------------------------------------

#P(C) = probability of class
#Here first one is done with all elements,
#totalTrainClass = len(allclassList)
totalTrainClass = n
probabilityClassList = []
logProbabilityClassList = []

for i in range(0,classLen):
    tempProbabilityClassList = classFreq[i]/totalTrainClass
    probabilityClassList.append(tempProbabilityClassList)
    logProbabilityClassList.append(-1 * math.log(probabilityClassList[i], 2))

#print("probabilityClassList")
#print(probabilityClassList)
#print("logProbabilityClassList")
#print(logProbabilityClassList)


#---------------------Line to word list-------------------------------
#List of words


tempWordList = []
wordList = []
allWorlCountList = []
for wordcut in range(0, n):
    tempstring = alldesList[wordcut]
    tempWordList= re.sub(r'[.!,;?]', ' ', tempstring).split() #-----split the words and kept them in the a temp list
    #print("-------------------------------")                 #---This list is then combined with the all word list
    #print(tempWordList)
    #print("-------------------------------")
    for wl in range(0, len(tempWordList)):
        wordprocess = tempWordList[wl]
        if wordprocess not in wordList and wordprocess not in stopList and len(wordprocess)>2:
            wordList.append(wordprocess)

#print("Wordlist")
#print(wordList)                     #------ wordList , all unique words are kept in here
totalUniWord = len(wordList)
#print(totalUniWord)
#print(totalTrainClass)
#print(classLen)



#-------------------------------------------------------------------------------------------------
#--------------------------------------word Frequency---------------------------------


wordfreq = []

for i in range(0,totalUniWord):
    wordfreq.append([int(0) for j in classList])

#print(wordfreq)

#print("All des list len")
#alldesListLen = len(alldesList)
alldesListLen = n

for i in range(0, alldesListLen):
    #checkwordfreq = wordList[i]
    tempdes2 = alldesList[i]
    #print("In Loop")
    #print(wordfreq)
    #print("-----------------------------------------------------------------------------------------------------------")
    #print("tempdes2 = " + tempdes2)
    tempWordList = re.sub(r'[.!,;?]', ' ', tempdes2).split()
    #print("tempWordList")
    #print(tempWordList)
    tcft = allclassList[i]
    #tcft = temp Class Frequency Table
    tempIndexClassFreq =  classList.index(tcft)
    for j in range(0,totalUniWord):
        checkwordfreq = wordList[j]
        #print("checkwordfreq " + checkwordfreq)
        checkfreqNumber = tempWordList.count(checkwordfreq)
        #print("checkfreqNumber "+str(checkfreqNumber))
        wordfreq[j][tempIndexClassFreq] = wordfreq[j][tempIndexClassFreq] + int(checkfreqNumber)

#print("Updated word freq")
#print(wordfreq)

#-------------------------- frequency of total number of words -------------------------------
totalWordFreq = []
for i in range(0, totalUniWord):
    totalWordFreqTemp = 0
    for j in range(0,classLen):
        totalWordFreqTemp = totalWordFreqTemp+wordfreq[i][j]
    totalWordFreq.append(totalWordFreqTemp)

#print(wordList)
#print(wordfreq)
#print(totalWordFreq)

probabilityword = []

for i in range(0,totalUniWord):
    probabilityword.append([int(0) for j in classList])

nLogProbabilityWord = []
for i in range(0,totalUniWord):
    nLogProbabilityWord.append([int(0) for j in classList])

#print(probabilityword)
epsilon = .1
for i in range(0,totalUniWord):
    for j in range(0, classLen):
        probabilityword[i][j] = ((wordfreq[i][j]/totalWordFreq[i]) + epsilon)/(1 + 2*epsilon)
        nLogProbabilityWord[i][j] = -1 * math.log(probabilityword[i][j],2)
        #if i==1 and j==2:
            #print("word freq " +str(wordfreq[i][j])+" Total WF "+ str(totalWordFreq[i])+" wf/twf "+ str(wordfreq[i][j]/totalWordFreq[i])+ " probabilityword "+ str(probabilityword[i][j]) + " nLogProbabilityWord[i][j] " + str(nLogProbabilityWord[i][j]))



#print(probabilityword)
#print(nLogProbabilityWord)
#print(wordList)



#------------------------------------------------------------------------------------------------------
#                                       Training Done
#------------------------------------------------------------------------------------------------------
#                                           Testing
#------------------------------------------------------------------------------------------------------

rCount=0

checkClassProbability = []
checkclassNProb = []

for iccp in range(0,classLen):
    checkClassProbability.append(0)
    checkclassNProb.append(0)



for i in range(n,pperson):
    for iccp in range(0,classLen):                                  #Len(classList) = classLen
        checkClassProbability[iccp] = probabilityClassList[iccp]
        checkclassNProb[iccp] = logProbabilityClassList[iccp]

    checkWordList = []
    checkName = person[i].split('\n', 2)[0]
    checkClass = person[i].split('\n', 2)[1]
    checkClass = checkClass.rstrip(' ')
    checkdes = person[i].split('\n', 2)[2]
    #print("checkdes")
    #print(checkdes)
    #checkdes = alldesList[i]
    tempCheckList = re.sub(r'[.!,;?]', ' ', checkdes).split()
    for w12 in range(0,len(tempCheckList)):
        checkprocess = tempCheckList[w12]
        #print(checkprocess+" "+tempWordList[w1])
        #if wordprocess not in wordList and wordprocess not in stopList and len(wordprocess)>2:
        if checkprocess not in checkWordList and checkprocess in wordList:
            checkWordList.append(checkprocess)
            p = wordList.index(checkprocess)
            for k in range(0,classLen):
                ##tempPW = float(str(probabilityword[p][k]))
                ##tempNLPW = float(str(nLogProbabilityWord[p][k]))
                ##tempCP = float(str(checkClassProbability[k]))
                ##tempNLP = float(str(checkclassNProb[k]))
                checkClassProbability[k] = float(checkClassProbability[k])*float(probabilityword[p][k])
                checkclassNProb[k] = float(checkclassNProb[k]) + float(nLogProbabilityWord[p][k])
                #print("checkclassNProb of "+ checkprocess +" is "+str(checkclassNProb[k])+ " for class "+str(classList[k]+" word "+ wordList[p]))
                ##tempCP = tempCP * tempPW
                ##tempNLP = tempNLP + tempNLPW
                ##checkClassProbability[k] = tempCP
                ##checkclassNProb[k] = tempNLP

    #print("tempCheckList")
    #print(tempCheckList)
    #print("checkWordList")
    #print(checkWordList)
    #print("ClassList")
    #print(classList)
    #print("nlog")
    #print(checkclassNProb)
    #print("prob")
    #print(checkClassProbability)
    rmin = min(checkclassNProb)
    #print(rmin)
    rindx = checkclassNProb.index(rmin)
    #print(rindx)
    r = classList[rindx]
    #print(r)
    actual2Probability = []
    for mm in range(0,classLen):
        actual2Probability.append(0)

    sumact = 0

    for mm in range(0,classLen):
        actual2Probability[mm] = 2**(checkclassNProb[mm]-rmin)
        sumact = sumact + actual2Probability[mm]

    actualProbability = []
    for nn in range(0,classLen):
        actualProbability.append(0)

    for nn in range(0,classLen):
        actualProbability[nn] = actual2Probability[nn]/sumact


    #print("a"+checkClass+"a")
    #print("a"+r+"a")

    if(r == checkClass):
        status = "Right"
        rCount = rCount+1

    elif(r!=checkClass):
        status = "Wrong"

    print(checkName+"   Predction : "+r+"    "+ status)
    #for ik in range(0,classLen):
    #    print(classList[ik]+": "+str(checkClassProbability[ik])+"  ", end =" ")
    #print("")
    #for ik in range(0,classLen):
    #    print(classList[ik]+": "+str(checkclassNProb[ik])+"  ", end =" ")
    #print("")
    for ik in range(0, classLen):
        print(classList[ik] + ": " + str(actualProbability[ik]) + "  ", end=" ")

    print("\n\n")

totalTest = pperson-n
print("Overall accuracy: "+str(rCount)+" of "+str(totalTest)+" = "+str(rCount/totalTest))





