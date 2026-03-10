nums=[1,2,3,2,4,7,4,5,9,7,6,8,3]
list1=set(nums)
list2=list(list1)
if len(list2)<=2:
    print(max(list2))
else:
    list2.remove(max(list2))
    list2.remove(max(list2))
    print(max(list2))