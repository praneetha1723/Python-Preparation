s=input().strip().lower()
i,j=0,len(s)-1
is_palindrome=True
while i<j:
    if s[i]!=s[j]:
        is_palindrome=False
        break
    i+=1
    j-=1
if is_palindrome:
    print(f"{s} is Palindrome")
else:
    print(f"{s} is not a Palindrome")




# str=input().lower()
# if str==str[::-1]:
#     print("Plaindrome")
# else:
#     print("Not Palindrome")