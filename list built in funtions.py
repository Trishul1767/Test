# list built in funtions
A=[1,2,3,4.5]
print(len(A)) # length of list
print(max(A)) # maximum element in list
print(min(A)) # minimum element in list
print(sum(A)) # sum of all elements in list
print(sorted(A)) # sorted list
print(sorted(A,reverse=True)) # sorted list in reverse order
print(list(reversed(A))) # reversed list
print(list(enumerate(A))) # list of tuples with index and element
print(list(zip(A,A))) # list of tuples with elements from two lists
print(list(map(str,A))) # list of strings of elements in list
print(list(filter(lambda x: isinstance(x,int),A))) # list of integers in list
print(list(filter(lambda x: isinstance(x,str),A))) # list of strings in list
print(list(filter(lambda x: isinstance(x,float),A))) # list of floats in list
print(list(filter(lambda x: isinstance(x,(int,str)),A))) # list of integers and strings in list
print(list(filter(lambda x: isinstance(x,(int,float)),A))) # list of integers andfloats in list
print(list(filter(lambda x: isinstance(x,(str,float)),A))) # list of strings andfloats in list
print(list(filter(lambda x: isinstance(x,(int,str,float)),A))) # list of integers,strings and floats in list
print(list(filter(lambda x: isinstance(x,(int,str,float,bool)),A))) # list of integers,strings, floats and booleans in list
print(list(filter(lambda x: isinstance(x,(int,str,float,bool,list)),A))) # list of integers,strings, floats, booleans and lists in list
print(list(filter(lambda x: isinstance(x,(int,str,float,bool,list,tuple)),A))) # list of integers,