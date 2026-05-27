# for i in (1,10)
# for i in range(1,10,3):
#     print(i)
# l=[1,2,3,4,5]
# for i in l:
#     print(i)
for i in range(50):
    print("hello world")


    
# n=int(input("enter n: "))
# #while loop 
# while n<10:
#     print(n)
#     n+=1


# Q2 reverse the number using loop

# n=int(input("enter the number"))
# digit = ""
# for i in str(n)[::-1]:
#  digit =digit +i
# print (digit) 


# Q2 reverse the number 
# n = int(input("Enter the number: "))
# reverse = 0

# while n != 0:
    
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print("Reversed number:", reverse)
   
# Q3 Find factorial using loop
n=int(input("enter the number"))
digit=1
for i in range(1,n+1):
    digit=digit*i
print(digit)