x=112211
if x < 0:
    print("invalid input")
else:
    rev = 0
    num = x
    while num != 0:
        remain = num % 10
        rev = rev * 10 + remain
        num //= 10
if rev == x:
    print("palindrome")
else:
    print("not palindrome")