import os
import re

print(os.getcwd())


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
print(person)
#--------------------------------------------------------------------------------------------


#===================-==================== word 2d list======================================================

word2D = []
numperson = len(person)-1

for i in range(0, numperson):
    word2D.append([j for j in person[i].split()])

print(word2D)

#-------------------2d array for freq table--------------------
classList = 3
wordlist = 10
wordfreq = []
for i in range(0, wordlist):
    wordfreq.append([int(0) for j in person])

print(wordfreq)