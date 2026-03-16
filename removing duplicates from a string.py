#removing duplicates from a string
n=input("Enter a string: ")
result=""
for i in n: 
    if i not in result: 
        result=result+i 
print("String after removing duplicates:", result)