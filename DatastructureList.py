#List 


a=12
b=13
c=14
d=15
e=16

#for creating list you have to use sqaure 
# brackets([])

l=[12,13,14,15,16]

#special powers
#1-hetrogeneous nature :-different type of data store kar skte hai at once

l=[12,"hello",44.5,True,print()]

# 2- ordered :- every element in the list has a designated position

# 3- mutable nature :- list ke andar kch bhi change kar skte hai delete ,change,add anything at any point of time

# 4- dupliactes:- you can store dupliactes elements inside 

# reading a list
# a= [10,20,30,40,50]
# print(a)
# print(a[4],a[-1])

# updating a list 
# a=[10,20,30 ,40 ,70]
# a[-1]=50
# print(a)
# print(a[4])

#delete a list
# a=[10,20,30 ,40 ,50]
# del a[-1] # a single element only 
# del a # this can delete a entire list
# print(a)

# a=[10,2,3,4,5,70]
# del a[-1]
# print(a)


# creating loops on list 
# a=[10,20,30,40,50]
#based on values 
# for i in a:
#     print(i)

# here you will access all the values 10,20,30...
# based on index
# for i in range(0,5):
# for i in range(0,len(a)):
#     print(a[i])
# output will be 10,20,30,40,50 
    
# this loop can access your index aswell
# as your values and it gives more control over your list 


#methods 
# a=[1,2,3,4]
# a.append([5,6,7])
# a.append(5)
# print(a)

# l=[]
# for i in range(10,51,10):
#     l.append(i)
# print(l) 

# l=[]
# for i in range(10,51,10): # for i in range(start,stop,step)
#     l.append(i)
# print(l)


# insert 
# a=[10,20,40,50]
# a.insert(2,30)
# print (a)

# # clear
a=[10,20,30,40,50]
saved = a.pop(0) # pop use index for delete
a.remove(10) # and remove use values
print(a)
print(saved)


#method in list
# .append()
# .remove()
# .insert()
# .pop()




#list comprehension 
# a=[1,2,3,4,5,6,7,8,9,10]


# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)


# b=[i for i in a if i%2==0]
# print[b]








