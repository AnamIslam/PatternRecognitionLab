from urllib.request import urlopen

#textpage = urlopen("https://cs.nyu.edu/faculty/davise/ai/tinyCorpus.txt")
textpage = urlopen("http://www.cs.nyu.edu/faculty/davise/ai/bioCorpus.txt")

n = str(textpage.read(), 'utf-8').split("\n\n")

print(n)
p = len(n)
print(p)
nameList = []
classList = []
desList = []
for i in range(1,p-1):
    #name,cls, des = n[i].split("\n")  #.split("\n")
    name = n[i].split('\n', 2)[0]
    cls = n[i].split('\n', 2)[1]
    des = n[i].split('\n', 2)[2]
    nameList.append(name.lower())
    classList.append(cls.lower())
    desList.append(des.lower())
    print(name)
    print(cls)
    print("---")
    print(des)

    #print(n[i])
    print("------------")

#print(str(textpage.read(), 'utf-8'))
print(nameList)
print(classList)
print(desList)