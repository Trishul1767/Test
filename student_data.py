student_data={}
n=int(input('enter number of students:'))
for i in range(n):
    p=int(input('enter pin:'))
    q=input('enter name:')
    d.update({p:q})
print(student_data)
#2)
l1=[1,2,3,4,5]
l2=['ram','Trishul','Sai','rahul','sujith']
fr={}
fr=zip(l1,l2)
print(dict(fr))
#3)
d={'a':1,'b':2,'c':3}
print('keys:',d.keys())
print('values:',d.values())
print('items:',d.items())