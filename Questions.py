# #Q1 IF ESLE 
# # To chech wether the number is even or odd 
# n=int(input("enter the number"))
# if n%2==0:
#     print("even number")
# else :
#     print ("odd number")


# #Q2 Student is pass or failed
# n=int(input("enter the marks"))
# if n>=34:
#     print ("student is pass")
# else :
#     print ("student is  fail ")

# # Q3 Check whether the number is +ve ,-ve,zero
# n=int(input("enter the number"))
# if n>0:
#     print ("number is +ve")
# elif n==0:
#     print("number is zero ")
# else :
#     print ("number is -ve")

# # Q4 check weather the user is teenager or adult 
# n=int(input("enter the age "))
# if n<13:
#     print ("child")
# elif n>=13 and n<=18 :
#     print ("teenager")
# else:
#     print ("adult")


# # Q5 check the maximum number from the three number
# n=int(input("enter the number one"))
# m=int(input("enter the number two"))
# l=int(input("enter the number three"))
# if n>=m and n>=l:
#     print ("one is greater")
# elif m>=n and m>=l:
#     print ("two is greater")
# else :
#     print (" three is greater")

# # vowels
# a=input("enter the letter")

# for a in ("aeiouAEIOU"):
#     print ("it is a vowel")

# # job eligibilty 
# Ex=int(input("enter the ex"))
# eduction=int(input("enter your education"))
# if Ex>=2 and eduction=={"graduated",75}:
#     print("elligible")
# else :
#     print ("not") 
     




# loops question 



# print the number from 1 to n
# n=int(input("enter the number"))
# for i in range(0,n):
#     print (i)





# Print even numbers from 1 to 20
# for i in range(0,21,2):
#     print (i)

# # Print numbers from 10 to 1
# n = int (input("enter the number"))
# digit=""
# for i in str(n)[::-1]:
#  digit=digit+i
# print (digit )




# n=input("enter the number")
# reverse=""
# for i in range(len(n)-1,-1,-1):
#     reverse=reverse+n[i]
# print(reverse)







# another approach
# n=int(input("enter the number"))
# rev=0
# while n!=0:
#    digit=n%10
#    rev=rev*10+digit
#    n=n//10
# print("reverse number",rev)





# Find factorial of a number
# n=int(input("enter the number"))
# fact=1
# for i in range(1,n+1):
#    fact=fact*i
# print (fact)


# n=int(input("enter the number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)




# Check if a number is palindrome
# n=int(input("enter the number"))
# rev=0
# copy=""
# while n!=0:
#     digit=n%10
#     rev=rev*10+digit 
#     n=n//10
   
# if copy==rev:
#     print ("pali")
# else:
#     print ("not pali")




# Q Check if a number is prime
# n=int(input("enter the number"))
# if n<=1:
#     print ("not a prime number")
# else:
#     for i in range(2,n):
#         if n%i==0:
#           print("not a prime number")
#           break
#     else :
#        print ("prime number")



#Q Print all prime numbers from 1 to 100
# for i in range (1,101):
#     if i>1:
#         for num in range(2,i):
#             if i%num==0:
#                 break
#         else :
#             print (i)



# for i in range(1,101):
#     if i>1:
#         for num in range(2,i):
#             if  i%num==0:
#                 break
        
#         else:
#             print(i)




#Fibonacci series using loop
# n= int (input("enter the number"))
# a=0
# b=1
# count=2
# while count<=n:
#     temp=b
#     b=b+a
#     a=temp
#     count +=1
# print(b) 
   



# counting occerency

# n=int(input("enter the number"))
# m=int(input("enter the occerency number"))
# count=0
# while n>0:
#     rem=n%10
#     if rem==m:
#         count+=1
#     n=n//10
# print  (count)




# remove duplicates
# L=[10,20,30,40,30,40,20,50,60,50 ,70,60,90,90,100,]
# unique=[]
 
# for i in L:
#     if i not in unique:
#        unique.append(i)
# print(unique)

  




# list question 

#Create a list and print all elements
# Find the length of a list
# Add an element to a list (append, insert)
# Remove an element from a list
# Access elements using index
# Check if an element exists in a list

#solution
# a=[10,20,30,40,50]
# for i in a:
#     # print(i)
# # for i in range(0,5): #using index
# #     print (i)
#     print(len(a))

# a=[10,20,30,40,50]
# a.append(90)
# a.insert(4,45)
# a.pop(4)
# print(a)


# a=[10,20,30,40,50]
# x=int(input("enter the number"))

# if x in a:
#     print("element found")
# else :
#     print("not found")






# Find the maximum and minimum element in a list
# n=[10,20,30,40,50]
# print(min(n))
# print(max(n))





#Reverse a list (without using built-in function)
# List=[10,20,30,40,50]
# rev=[]
# for i in range(len(List)-1,-1,-1):
#     """
#     len(list)-1=5-1=4 last index
#     -1=stop it will stop before -1
#     -1= step means backward direction 

#     """
#     rev.append(List[i])
# print(rev)



# LIST=[10,30,40,50,20]
# LIST.reverse()
# print(LIST)


# #Sort a list (ascending and descending)
# a=[50,40,23,1,4,7,347]
# a.sort()
# print(a)






# largest question and second largest question 
# a=[234,563,6434,563,90,23467,23]
# Largest=a[0]
# Second_largest=a[0]
# Largest_index=0
# Second_index=0
# for i in range(1,len(a)):
#     if a[i]>Largest:
#         Second_largest=Largest
#         Second_index=Largest_index
#         Largest=a[i]
#         Largest_index=i
#     elif a[i]>Second_largest:
#         Second_largest=a[i]
#         Second_index=i
# print(f"the largest element in the list:-{Largest} and the index of largest element in the list :-{Largest_index}")
# print(f"the  second largest element in the list:-{Second_largest} and the index of second largest element in the list :- {Second_index}")
 






# Smallest and Second smallest question 

# a=[1,0,23,45,56,67]
# Smallest=a[0]
# Second_Smallest=a[-1]
# Smallest_index=0
# Second_index=0
# for i in range(1,len(a)):
#     if a[i]<Smallest:
#         Second_Smallest=Smallest
#         Second_index=Smallest_index
#         Smallest=a[i]
#         Smallest_index=i
#     elif a[i]<Second_Smallest:
#         Second_Smallest=a[i]
#         Second_index=i
# print(f"the Smallest element in the list:-{Smallest} and the index of Smallest element in the list :-{Smallest_index}")
# print(f"the  second Smallest element in the list:-{Second_Smallest} and the index of second Smallest element in the list :- {Second_index}")




# l=[1,1,1,2,2,2,3,4,5,5,5,5,6,6,6]
# count=0
# for i in l:
#     if i==2:
#         count=count+1
# print(count)

# palindrome in list
# l = [1, 2, 3, 15, 14, 3, 2, 1]
# if l == l[::-1]:
#     print("Palindrome") 
# else:
#     print("Not a palindrome")



#27) Seprate each digit of a number and print it on the new line
# num=int(input("enter the number"))
# while num>0:
#     digit=num%10
#     print(digit)
#     num=num//10

#26)  Accept a number and check if it a perfect number or not.

# num =int(input("enter the number"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum +=i

# if sum==num:
#     print("perfect number")
# else:
#     print("not a perfect number")

#25) sum of factors

# num=int(input("enter the number"))
# sum=0
# for i in range (1,num):
#     if num%i==0:
#         sum +=i
# print (sum )


#24) Print all the factors of a number.

# num=int(input("enter the number"))

# for i in range(1,num): 
#     if num %i==0:
#         print(i)


#22) Print the sum of all even & odd numbers in a range seperately.

# start=int(input("enter the number"))
# stop=int(input("enter the end number"))
# even=0
# odd=0
# for i in range(start,stop+1):
#     if i %2==0:
#         even +=i
#     else:
#         odd +=i

# print("sum of even:",even)
# print("sum of odd:",odd)


#21) Factorial of a number

# n=int(input("enter the number"))
# fact=1

# for i in range(1,n+1):
#     fact=fact*i
    
# print (sum)


# n=int(input("enter the number"))
# fact=1
# for i in range(1,n+1):
#    fact=fact*i
# print (fact)



# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)



#fabonaci series

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# print("Fibonacci Series:")

# for i in range(n+1):
#     print(a)
 
#     c = a + b
#     a = b
#     b = c


                # or

# n=int(input("enter number: "))
# a=0
# b=1
# for i in range(n):
#      print(a)
#      a,b=b,b+a



#prime number
# num=int(input("enter the number"))
# if num<=1:
#      print ("not a prime number")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("not a prime number")
#             break
#     else:
#         print("prime number")

    
# # Print all prime numbers from 1 to 100
# for i in range(1,101):
#     if i>1:
#         for i in range(2,i):
#             if num%i==0:
#                 break
               
#             else:
#                 print(i)


# Strong number
"""num = int(input("Enter a number: "))

temp = num
sum = 0

while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum += fact
    num = num // 10

if sum == temp:
    print("Strong Number")
else:
    print("Not a Strong Number")"""


# palindrome
"""num=int(input("enter the number"))
copy=num
digit=0

while num>0:
    digit=digit*10+num%10
    num=num//10

if copy==digit:
        print("palindrome")
else:
        print("not a palindrome")"""





    








#find duplicates in the elements
lst = [1,2,3,4,1,2,5]

dup = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            if lst[i] not in dup:
                dup.append(lst[i])

print(dup)
# lst = [1,2,3,4,1,2,5]

# dup = []

# for i in lst:
#     if lst.count(i) > 1 and i not in dup:
#         dup.append(i)

# print(dup)