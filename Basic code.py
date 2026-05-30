# fun app code
print("Hello, World!")
print("This is a fun app!")
print("Enjoy coding!")
# a gaming app code
print("Welcome to the gaming app!")
print("Get ready to play!")
print("Have fun gaming!")
# a social media app code
print("Welcome to the social media app!")
print("Connect with friends and family!")
print("Share your moments and memories!")
import random
def generate_random_number():
    return random.randint(1, 100)
print("Random number between 1 and 100:", generate_random_number())
def calculate_sum(a, b):
    return a + b
print("The sum of 5 and 10 is:", calculate_sum(5, 10))
def greet_user(name):
    return f"Hello, {name}! Welcome to the app!"
print(greet_user("Alice"))
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
print("Factorial of 5 is:", calculate_factorial(5))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Is 7 a prime number?", is_prime(7))
print("Is 10 a prime number?", is_prime(10))
def reverse_string(s):
    return s[::-1]
print("Reversed string of 'Hello' is:", reverse_string("Hello"))
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)
        return fib_sequence
print(fibonacci(n))
