# tuple built in functions
T=(1, 2, 3, 4, 5)
print(len(T))  # length of the tuple
print(max(T))  # maximum value in the tuple
print(min(T))  # minimum value in the tuple
print(sum(T))  # sum of all elements in the tuple
print(T.count(3))  # count of occurrences of 3 in the tuple
print(T.index(4))  # index of the first occurrence of 4 in the tuple
# tuple slicing
print(T[1:4])  # slice from index 1 to 3
print(T[:3])  # slice from the beginning to index 2
print(T[2:])  # slice from index 2 to the end
print(T[-3:])  # slice the last three elements
print(T[::2])  # slice with a step of 2 (every other element
print(T[::-1])  # reverse the tuple

print(T)  # original tuple remains unchanged

