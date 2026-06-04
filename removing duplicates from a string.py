#removing duplicates from a string
n=input("Enter a string: ")
result=""
for _ in n: 
    if _ not in result: 
        result=result+_
print("String after removing duplicates:", result)
