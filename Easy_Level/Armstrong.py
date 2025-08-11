number=int(input("Enter a Number: "))
length=len(str(number))
temp=number
total=0
while temp>0:
    digit=temp%10
    total+=digit**length
    temp=temp//10
print(f"Number is {number} and Total is {total}")
if number==total:
    print(f"{number} is Armstrong.")
else:
    print(f"{number} is not Armstrong.")



