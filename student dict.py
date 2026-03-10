'''student=[]
n=int(input('enter number of students:'))
for i in range(n):
    rollnumber=input('enter rollnumber:')
    name=input('enter name:')
    marks=int(input('enter marks:'))
    student.append({'rollnumber':rollnumber,'name':name,'marks':marks})
print(student)
student=[
    {'rollnumber':1,'name':'sumalatha','marks':90},
    {'rollnumber':2,'name':'trishul','marks':95},
    {'rollnumber':3,'name':'sumanth','marks':85}  
]
n=int(input('enter the rollnumber:'))
i=0
for j in student:
    if j['rollnumber']==n:
        print('student details:',j) 
        i=i+1   
        break
if i==0:
    print('student details not found')
l1=[1,2,3,5,4,6,8,7,9]
m=l1[1]
for i in range(len(l1)):
    if m<l1[i]:
        m=l1[i]
    else:
        pass
print(m)'''
student=[
    {'rollnumber':1,'name':'sumalatha','marks':90},
    {'rollnumber':2,'name':'trishul','marks':95},
    {'rollnumber':3,'name':'sumanth','marks':85}  
]
m=student[0]['marks']
for i in student:
    if m<i['marks']:
        m=i['marks']
    else:
        pass
print(m)