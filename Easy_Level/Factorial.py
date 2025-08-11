def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
num=int(input("Enter a Number: "))
print(f"Factorial of {num} is {factorial(num)}")


# n=int(input("Enter a Value: "))
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(f"Factorial of {n} is {fact(n)}")