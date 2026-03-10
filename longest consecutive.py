l=[1,2,3,1,2,3,4,1,3]
max=[]
current=[]
for i in range(1,len(l)):
    if l[i]==l[i-1]+1:
        current.append(l[i])
    else: 
        if len(current)>len(max):
            max=current
        current=[l[i]]
if len(current)>len(max):    
    max=current
print(max)
    