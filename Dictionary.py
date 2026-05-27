# a=[12,34,53,3,23,78]  #list

# d={} #dictionary
# print (type(d))

# d={1,2,3} # set
# print(d)

# d={"one":1,"two":2,"three":3}

# """ one two three are keys"""

# print(d["three"])
 

# d1={1:20,2:20,3:30}
# d2={4:40,5:50,6:60}

# for i in d1:
#     print(i)  # accesssing keys
#     print(d1[i]) # accessing values




# d1={1:20,2:20,3:30}
# d2={3:40,5:50,6:60}

# # for i in d2:
# #     d1[i]=d2[i]
# # print(d1)


# for i in d2:
#     if i in d1.keys():
#         d1[i]=d1[i] + d2[i]
#     else:
#         d1[i]=d2[i]

# print(d1)

# find frequency
l=[1,1,1,2,2,2,3,4,5,5,5,5,6,6,6]

d={}

for i in l:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)








