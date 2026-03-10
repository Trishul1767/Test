# plus one to the list
list=[1,2,3]
list1=[]
list2=[]
num=0
for i in list:
    num=num*10 + i
num1=num+1
#for now. reversed list
while num1!=0:
    remain=num1%10
    list1.append(remain)
    num1//=10
# reversing the list1 to get the final answer
list2=list1[::-1]
print(list2)
