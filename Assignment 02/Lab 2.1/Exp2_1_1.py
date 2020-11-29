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
print("stopList")
print(stopList)


#Corpustext read
#f = open("corpus.txt", "r")
#full = f.read()
#print(full)
#===========================================================================
#personList = []
#with open('corpus1.txt','r') as corpus:
#    for line in corpus:
#        for person in line.split("\n\n"):
#           personList.append(person)
#           #print(word)
#
#print(personList)
#print(len(personList))
#===========================================================


#---------------------------------corpus text read------------------------------------
with open("corpus1.txt") as f1:
    lines = f1.read()


#--------------------------------- spliting by paragraph---------------------------------
person = lines.split("\n\n")
print(person)
print(len(person))
for lenperson in range(0,len(person)-1):
    tempPerson = person[lenperson].lower()
    tempPerson = tempPerson.strip()

    person[lenperson]=tempPerson

print("---------")
print("Person all in Lower case")
print(person)
#--------------------------------------------------------------------------------------------
classList = []
allclassList = []
allnameList = []
alldesList = []

for i in range(0,len(person)-1):
    tempName = person[i].split('\n', 2)[0]                      #---Spliting the names
    tempClass = person[i].split('\n', 2)[1]                     #--- Spliting the ClassNAmes
    tempClass = tempClass.rstrip(' ')
    tempDes = person[i].split('\n', 2)[2]                       #---Spliting the descriptions
    allclassList.append(tempClass.lower())
    allnameList.append(tempName)
    alldesList.append(tempDes)
    TCLen = len(tempClass)                                      #---------make a class list
    #print(tempClass)
    #print(TCLen)
    #if tempClass[TCLen]==' ':
    #    tempClass = tempClass[:-1]
    #tempClass = tempClass.rstrip(' ')                           # removing space
    #allclassList.append(tempClass)
    if tempClass not in classList:
        classList.append(tempClass.lower())

print("Class List")
print(classList)
print("All Class List")
print(allclassList)
print("All Name List")
print(allnameList)
print("All Description List")
print(alldesList)



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

print(classList)
print(classFreq)

#P(C) = probability of class
#Here first one is done with all elements,
totalTrainClass = len(allclassList)
probabilityClassList = []
for i in range(0,classLen):
    tempProbabilityClassList = classFreq[i]/totalTrainClass
    probabilityClassList.append(tempProbabilityClassList)

print(probabilityClassList)


#---------------------Line to word list-------------------------------
#List of words
tempWordList = []
wordList = []
allWorlCountList = []
for wordcut in range(0, len(alldesList)-1):
    tempstring = alldesList[wordcut]
    tempWordList= re.sub(r'[.!,;?]', ' ', tempstring).split() #-----split the words and kept them in the a temp list
    #print("-------------------------------")                 #---This list is then combined with the all word list
    #print(tempWordList)
    #print("-------------------------------")
    for wl in range(0, len(tempWordList)):
        wordprocess = tempWordList[wl]
        if wordprocess not in wordList and wordprocess not in stopList and len(wordprocess)>2:
            wordList.append(wordprocess)

print("Wordlist")
print(wordList)                     #------ wordList , all unique words are kept in here
totalUniWord = len(wordList)
print(totalUniWord)
print(totalTrainClass)
print(classLen)


#--------------------word Frequency---------------------------------
wordfreq = []

for i in range(0,totalUniWord):
    wordfreq.append([int(0) for j in classList])

print(wordfreq)

print("All des list len")
alldesListLen = len(alldesList)

for i in range(0, alldesListLen):
    #checkwordfreq = wordList[i]
    tempdes2 = alldesList[i]
    print("In Loop")
    print(wordfreq)
    print("-----------------------------------------------------------------------------------------------------------")
    print("tempdes2 = " + tempdes2)
    tempWordList = re.sub(r'[.!,;?]', ' ', tempdes2).split()
    print("tempWordList")
    print(tempWordList)
    tcft = allclassList[i]
    #tcft = temp Class Frequency Table
    tempIndexClassFreq =  classList.index(tcft)
    for j in range(0,totalUniWord):
        checkwordfreq = wordList[j]
        print("checkwordfreq " + checkwordfreq)
        checkfreqNumber = tempWordList.count(checkwordfreq)
        print("checkfreqNumber "+str(checkfreqNumber))
        wordfreq[j][tempIndexClassFreq] = wordfreq[j][tempIndexClassFreq] + int(checkfreqNumber)

print("Updated word freq")
print(wordfreq)



#-------------------------- frequency of total number of words -------------------------------
totalWordFreq = []
for i in range(0, totalUniWord):
    totalWordFreqTemp = 0
    for j in range(0,classLen):
        totalWordFreqTemp = totalWordFreqTemp+wordfreq[i][j]
    totalWordFreq.append(totalWordFreqTemp)

print(wordList)
print(wordfreq)
print(totalWordFreq)

probabilityword = []

for i in range(0,totalUniWord):
    probabilityword.append([int(0) for j in classList])

nLogProbabilityWord = []
for i in range(0,totalUniWord):
    nLogProbabilityWord.append([int(0) for j in classList])

print(probabilityword)
epsilon = .1
for i in range(0,totalUniWord):
    for j in range(0, classLen):
        probabilityword[i][j] = ((wordfreq[i][j]/totalWordFreq[i]) + epsilon)/(1 + 2*epsilon)
        nLogProbabilityWord[i][j] = -1 * math.log(probabilityword[i][j],2)
        if i==1 and j==2:
            print("word freq " +str(wordfreq[i][j])+" Total WF "+ str(totalWordFreq[i])+" wf/twf "+ str(wordfreq[i][j]/totalWordFreq[i])+ " probabilityword "+ str(probabilityword[i][j]) + " nLogProbabilityWord[i][j] " + str(nLogProbabilityWord[i][j]))



print(probabilityword)
print(nLogProbabilityWord)
print(wordList)

#------------------------------------------------------------------------------------------------------
#                                       Training Done
#------------------------------------------------------------------------------------------------------
#                                           Testing
#------------------------------------------------------------------------------------------------------



