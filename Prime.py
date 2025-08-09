def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

n=int(input("Enter a Number: "))
if is_prime(n):
    print(f"{n} is Prime Number.")
else:
    print(f"{n} is not a Prime Number.")