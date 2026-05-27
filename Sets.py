""" 
properties of set
1)sets are unorder (no indexing )
 2)mutable (can add ,but cannot change or remove)
 3)unique elements (no duplicates)
 4)heterogeneous(can contain different data types)
 """



# a=[]
# b={}
# c=set() # type conversion

# s=set() #empty set
# s={1,2,3,4,5}
# print(s)

# s=set() #empty set
# s={1,2,3,4,4,5,5}
# print(s)

# methods in sets
"""
1.add()
2.update()
3.clear()
4.pop()
5.discard()
6.remove()
"""

#1 add() # for adding single element /value
# s={1,2,3,4,5}
# s.add(6)
# print(s)

# #2 update # for adding multiple elements/values
# s.update([6,7,8])
# print(s)

#3 reomve() # if values is not present we will get an error 
# s.remove(4)
# print(s)

#4 discard() 
# s.discard(10)
# print(s)

#5 pop() # remove smallest element from the sets
# s.pop()
# print(s)

# # 6. clear() #remove all the elemnts and gives us an empty set
# s.clear()

"""
1 intersection
2 union
3 difference
4 symmetric difference
"""

# s1={1,2,3,4}
# s2={2,3,4,5}
# print(s1.intersection(s2))
# print(s1.union(s2))

# # ese element jo s1 mei present hai but s2 mei nhi hai usko diiference bolenge 
# print(s1.difference(s2))
# print(s2.difference(s1))

# print(s1.symmetric_difference(s2))


# fs={1,2,3,4,5,6}
# fs=frozenset(fs) # frozenset is a function
# fs.add(60)
# fs.remove(10)
# print(fs)






