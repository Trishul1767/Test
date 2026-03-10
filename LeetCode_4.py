list1=[-5,-8,-3,-1,0,1,3,4,5,6,4,9]
print(sorted(list(map(lambda x: x*x, list1))))

# Two pointer approach

n=len(list1)
right=n-1
left=0
result = [0]*n
for i in range(n-1,-1,-1):
    sqr_right= list1[right] * list1[right]
    sqr_left = list1[left] * list1[left]
    if sqr_left > sqr_right:
        result[i]=sqr_left
        left+=1
    else:
        result[i]=sqr_right
        right-=1
print(result)