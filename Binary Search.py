l1=[1,2,3,4,5,6,7,8,9,10,12,13,14]
n=int(input("Enter the number to search: "))
l=len(l1)
high=len(l1)-1
low=0
while low<=high:
    mid=(low+high)//2
    if l1[mid]==n:
        print("Element found at index: ",mid)
        break   
    elif l1[mid]>n:
        high=mid-1
    else:
        low=mid+1
else:    print("Element not found in the list.") 