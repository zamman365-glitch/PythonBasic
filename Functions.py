# # bar bar koi cheez na likhne padhe isiliye function use karte hai 
# # user defined functions

# def greeting(): #defining of a function 
#      print ("hello good morning ")

# greeting () # calling of a function 


# # parameters and arguments 

# def addition(a, b):
#     print(a + b)

# addition(10, 20) 

# def pali(n):
#      rev=0
#      copy =n
#      while n !=0:
#           rev= rev*10+n%10
#           n=n//10
          
#           if copy==rev:
#                print ("palindrome")

#           else :
#                print ("not a palindrome ")

#                pali(121)
#                pali(123)
#                pali(19191)


# # 1st positional argument

# def multiply(a,b):
#      print (a*b)

#      multiply (12,67) # fixed positional arguments 



#      #default arguments /keyword arguments 

#      def info (name , age ):
#           print ("your name is {name} and your age is { age}")

#           info (age=24,name="zamman ")

# # if u give a value using default argument you always
# # have to give further values using default arguments
#           def info (a,b,c,d):
#                print (a,b,c,d)

#                info(12,34,c=65,d=78)

  
#   #default parameter / keyword parameter

# def info(name,age,id=None):
#      print ("info recieved")

# info ("akarsh" ,24,)



# #Q2 febonacci 
# # n= int (input("enter the number"))
# # a=0
# # b=1
# # count =2
# # while count<n:
# #      temp =b
# #      b=b+a
# #      a=temp
# #      count=count+1
# #      print(b)


# n=int(input("enter number: "))
# a=0
# b=1
# for i in range(n):
#      print(a)
#      a,b=b,b+a


# def strongnumber(n):
#      sum=0
#      copy=n
#      while n>0:
#           z=n%10
#           fact=1
#           for i in range (1,z+1):
#                fact=fact*1

#           sum =sum +fact
#           n=n//10

#      if sum==copy:
#           print (copy)

#      for i in (1,1001):
#           print (copy )




# # return vs print 

"""def hello ():
    return "how are you "

print (hello())
"""

# def agechecker(n):
#     if n >=18:
#         return True
#     else:
#         return False 
    

    
# age =int (input("enter your age:-"))

# if agechecker(age):
#      print ("cannot vote")
# else:
#      print ("cannot vote")


# #stack
# def hello1():
#     hello2()
#     print("hello1")
       
# def hello2():
#     hello3()
#     print("hello2")

# def hello3():
#     hello4()
#     print("hello3")

# def hello4():
#     print("hello4")

# hello1()    


# #recursion 

def numbers(n):
    if n==101:
        return "done"
    print(n)
    numbers(n+1)

numbers(1)    


# #backtracking process 
# def numbers(n):
#     if n==101:
#         return "done"
#     numbers(n+1)
#     print(n)
    
# numbers(1)    






                                       # args
# how can we add two number

# def addition(a, b):
#     print(a + b)

# addition(10, 20) 

"""
problems is what if hum hi nhi pata ki kitne parameters hone wale hai 
solution->args
"""

"""
args-> *variable_ name
variable_name = kch bhi ho skta hai
args value ko accept karte hai in the form tuple
"""

"""
def add(*lolo):
    print(type(lolo))
    print(lolo)
add(10,20,30,40,50)

     

def add(*chacha):
    for i in chacha:
        print(i)
add(10,20,30,40,50)

"""






                               #kwargs

"""
def polio(name,age,pin,contact):
    print(name,age,pin,contact)
polio(name="zamman",age=20,pin=1222,conatct=1234567890,grandfather="lala")
#inhe hum bolte hai keywords arguments
"""




"""
kwargs -> keywords arguments , no of arguments and parameters nhi pata ho isliye kwargs use karte hai
denotes -> **variables_name= Ramesha,lolo,etc
kwargs -> accept karta hai sari ko in the form of dictationary
parameters=keys
arguments=values
"""


"""
def polio(**variables):
    print(type(variables))
    print(variables)
polio(name="zamman",age=20,pin=1222,conatct=1234567890,grandfather="lala")
"""
 


"""

def polio(**a):
    for i in a:
        print(f"Parameter->{i} and Arguments->{a[i]}")
        # i= dict keys ,a[i]= un keys ki values
   
polio(name="zamman",age=20,pin=1222,conatct=1234567890,grandfather="lala")


"""



                                   # LAMBDA FUNCTION
"""
lamba function-> jab ek function ek line mei aa jaye
lambda=keyword ek variables ko convert kiya function mai 
a,b :a+b -> agar a and b variables mei kch value aayegi toh hi a+b chalega warna nhi chalega
"""

# add=lambda a,b: a+b 
# print(add(10,20))



# def lolo(**kwargs):
#     print(kwargs.keys())
# lolo(city='Bhopal',state='mp')

# check=lambda a :"even" if a%2==0 else "odd" 
# print(check(int(input("enter the number"))))

# Greatest = lambda a, b: a if a > b else b

# print(Greatest(
#     int(input("Enter number a: ")),
#     int(input("Enter number b: "))
# ))

data = {'a':10, 'b':50, 'c':20}

max_key = max(data, key=data.get)

print(max_key)

# Convert=lambda a : a.upper() 
# print(Convert(input("enter the String")))