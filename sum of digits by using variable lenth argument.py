def sum_digits(*n):
    total=0
    for number in n:
        for digit in str(abs(number)):
            total+=int(digit)       
    return total
    pass    
# Write a function that takes any number of integer arguments and returns the sum of all their digits.