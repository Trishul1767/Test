n=int(input('enter the number of values: '))
fr={}
for i in range(n):
    key=input('enter rollnumber:')
    value=input('enter name:')
    fr[key]=value   
print(fr)
for i in fr:
    print(i)