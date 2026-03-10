def is_prime(n):
    count = 0
    for i in range(2,n):
        if n % i == 0:
            count += 1  
    if count == 0:
        print("The number is prime")
    else:
        print("The number is not prime")

def harshad_number(n):
    x=n
    add=0
    while n!=0:
        remain=n%10
        add=add+remain  
        n=n//10
    if x%add==0:    
        print("The number is a Harshad number")   
    else:
        print("The number is not a Harshad number")

def sum_digits(n):
    sum=0
    while n>0:
        remain=n%10
        sum=sum+remain
        n=n//10
    print("The sum of digits is",sum)

def sum_fd_ld(n):
    ld=n%10
    while n>=10:
        fd=n//10
    print("The sum of first and last digit is",fd+ld)

def neon(n):
    sq=n*n
    sum=0
    while sq>0:
        remain=sq%10
        sum=sum+remain
        sq=sq//10
    if sum==n:
        print("The number is a Neon number")
    else:
        print("The number is not a Neon number")

if __name__ == "__main__":    
    n = int(input("Enter a number: "))
    print("enter '1' to check prime number, '2' to check harshad number, '3' to sum of digits, '4' to sum of first and last digit, '5' to check neon number  ")
    op = int(input("Enter the operation"))
    match op:
        case 1:
          is_prime(n)
        case 2:
          harshad_number(n)
        case 3:
         sum_digits(n)
        case 4:
         sum_fd_ld(n)
        case 5:
         neon(n)
        case _:
          print(("invalid operation"))
