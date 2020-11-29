import urllib.request
import re


def getWordsFromURL(url):
    return re.compile(r'[\:/?=\-&]+',re.UNICODE).split(url)

#target_url = "https://cs.nyu.edu/faculty/davise/ai/tinyCorpus.txt"
#target_url = "http://www.cs.nyu.edu/faculty/davise/ai/bioCorpus.txt"
target_url = "https://raw.githubusercontent.com/Simdiva/DSL-Task/master/data/DSLCC-v2.0/test/test.txt"

#print(words)
line = []
for n in urllib.request.urlopen(target_url):
    #words = getWordsFromURL(target_url)
    line =n;

    print(line)
    #wordCount = len(words.)
    #line.append(n)

#print(line)