#to check what added to b from a
s='trisha'
t='trishal'
fr={}
fr1={}
for i in s:
    if i in fr:
        fr[i]+=1
    else:
        fr[i]=1
for i in t:
    if i in fr1:
        fr1[i]+=1
    else:
        fr1[i]=1
l1=[]
l2=[]
for i in fr:
    l1.append(i)
for i in fr1:
    l2.append(i)
if len(l1)==len(l2):
    for keys in fr.keys():
        if fr[keys]!=fr1[keys]:
            print(keys)
        else:
            pass
else:
    for i in t:
        if i not in s:
            print(i)
        else:
            pass
