# a='milind thorat'
# print(a[2:5:2])
# # indexing in list [start:stop:step]

# s="zamman"
# print(s[::-1])
# print (len(s))
# print(f'String in upper format-> {s.upper()}')
# print(f'String in lower format->{s.lower()}')


# Q32) Arrange string characters such that lowercase letters should come first
# s="SHEry"
# lower=""
# upper=""
# for i in s:
#     if i.islower():
#         lower=lower+i
#     elif i.isupper():
#         upper=upper+i
# print(lower+upper)




# 33) Count all letters, digits, and special symbols from a given string
    # Given: str1 = "P@#yn26at^&i5ve"
    # Expected Outcome:
    # Total counts of chars, digits, and symbols
    # Chars = 8
    # Digits = 3
    # Symbol = 4
 
# str1 = "P@#yn26at^&i5ve"
# alpha=0
# digit =0
# symbol=0
# for i in str1:
#     if i.isalpha():
#         alpha=alpha+1
#     elif i.isdigit():
#         digit=digit+1
#     else:

#         symbol=symbol +1

# print(f'Alphabet={alpha}')
# print (f"digit={digit}")
# print (f"symbol={symbol}")

# Q34 Compare two strings without using inbuilt functions
# str1="hello"
# str2="hello"
# if len(str1)==len(str2):
#     for i in range (len(str1)):
#      if str1[i]!=str2[i]:
#         print("String are not same")
#         break
#     else :
#      print("string are same")
# else:
#    print("both string are of not the same lenght")



# Q35 Count Vowels from given string 
# def countvowels():
#    str1="aeiou"
#    vowels="aeiouAEIOU"
#    count =0
#    for i in str1:
#      if i in vowels:
#        count=count+1
#    return f"total count of vowels are={count}"
# print(countvowels())


# 36) Reverse a string
 
# n=str(input("enter the letter"))
# digit=""
# for i in str(n)[::-1]:
#     digit =digit+i
# print(digit)


s = ["h","e","l","l","o"]
digit=""
for i in s[::-1]:
    digit=digit+i
print(digit)
    
s.reverse()

#  37) Check string is Pallindrome or not**
# def pailndrome(s):
    
#     rev=s[::-1]
#     if s==rev:
#      print(f"{s} is an palindrome")
#     else:
#      print(f"{s} is not a palindrome")
# pailndrome("madam")



# string = input("Enter a string: ")

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# count no of vowels and consonats from a string

# str1="zamman"
# vowels="aeiouAEIOU"
# count =0
# consonants=0
# for i in str1:
#     if i in vowels:
#      count=count+1
#     else:
#         consonants +=1
# print (f"total vowels are:{count}")
# print (f"total consonants are:{consonants}")


# a = "kalu"
# for i in a [::-1]:
#     print(i)


# word=s.strip().split()
# return (s.word([-1]))
# strip= Remove extra spaces from the beginning and end using strip().
# split=Split the string into words using split()