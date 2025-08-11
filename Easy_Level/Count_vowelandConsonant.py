str=input("Enter String: ").strip().lower()
vowels="aeiou"
vowel_count=0
consonant_count=0
for char in str:
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print("Vowel Count: ",vowel_count)
print("Consonant Count: ",consonant_count)


# str=input("Enter String: ").lower()
# vowel="aeiou"
# vowel_count=sum(1 for char in str if char in vowel)
# consonant_count=sum(1 for char in str if char.isalpha() and char not in vowel)
# print("Vowel Count: ",vowel_count)
# print("Consonant Count: ",consonant_count)