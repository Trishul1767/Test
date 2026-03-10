'''n=int(input("Enter a number:"))
def prime(n):
    if n<=1:
        return ""
print(prime(n))'''



n = int(input("Enter a number: "))

def prime(n):
    # 0 and 1 are not prime numbers
    if n <= 1:
        return "Not Prime"
    
    # Check for factors from 2 up to n-1
    for i in range(2, n):
        if n % i == 0:
            # If we find ANY factor, it is not prime.
            return "Not Prime" 
            
    # If the loop finishes without finding a factor, it is prime.
    return "Prime"

print(prime(n))



n = int(input("Enter a number: "))

def print_primes_upto(n):
    # Loop through every number from 2 to n
    for number in range(2, n + 1):
        is_prime = True
        
        # Check if the current 'number' has divisors
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break # Stop checking this number
        
        if is_prime:
            print(number)

print_primes_upto(n) 

            
        