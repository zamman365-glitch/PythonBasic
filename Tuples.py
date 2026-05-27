# Tuples
"""
1. tuples are ordered(indexing)
2. tuples have duplicacy
3. Are heterogenous
4. Are Immutable
"""

# t=() #  empty tuple
# t=(1,2,3,4,5)
# t[2]=10
# print(t)


# for i in t:  direct loop 
#     print(t)

# for i in range (len(t)):  index loop
#     print(i,t[i])


# for index, value in enumerate(t):
#     print(index,value)


# t=(1,2,3,4,5)
# print(t[2])
# print(t[1:4])


"""
methods in tuples
1. count() we can count occurence of values
2. index()

"""

#  t=(1,2,2,3,3,4,3,2,3,4,5,6)


# print(t.count(2))

# print(t.index(6))

# print(3 in t)  # member ships operator



# tuple unpacking and packing
"""  t=(1,2,3,4,5)  # this is unpacking
 a,b,c,d,e=t
 print(a)
 print(b)
 print(c)
 print(d)
 print(e)

a=1,2  # this is packing
 """


# star expression
# t=(1,2,3,4,5)
# a,*b,c= t
# print(a)
# print(b) # middle value extraction 
# print(c)

# t=(1,2,3,4,5)
# a,*_,c=t
# print(a)
# print(c)

# merge two tuples
t1=(1,2,3)
t2=(4,5,6)
print(t1 + t2)






