#38) Accept List elements and reprint it
# a=int(input("how many elements u wants"))

# l=[]

# for i in range(a):
#     z=int(input("tell your number"))
#     l.append(z)

# print(l)

# a=eval(input("tell your str"))
# print (a)


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


# a=[10,20,30,40,50]
# z=len(a)-1

# for i in range(len(a)//2):
#     a[i],a[z]=a[z],a[i]
#     z=z-1
# print(a)



# 40) Print positive and negative elements of an List
# a=[10,20,30,40,50,-3,5,-2]
# for i in a:
#     if i>=0:
#         print(i)
# for i in a :
#     if i<=0:
#         print(i)

# find sorting of list in ascending order and in descending order

# num =[20,30,40,50,60]

# num.sort()
# print("ascending order",num)
# num.sort(reverse=True)
# print("descending order",num)

# bubble sort 
# a=[56,32,256,7,5,2,90] 

# for j in range(len(a)-1):
#     for i in range(0,len(a)-1-j):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print(a)

#  Q44 Find the greatest element and print its index too.
  #  {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index
# a=[2, 96, 69, 77, 145, 20] 

# largest=a[0]
# index=0
# for i in range(1,len(a)):
#     if a[i] > largest:
#         largest =a[i]
#         index =i
# print(f"largest element is {largest} at index {index}")

#46) Find the second greatest element0 
  #  {2, 96, 69, 77, 145, 20} = Second greatest element = 96
# l=[2, 96, 69, 77, 145, 20]
# largest=l[0]
# li=0
# s_largest=l[0]
# si=0
# for i in range(1,len(l)):
#     if l[i]>largest:
#         s_largest=largest
#         largest=l[i]
#         sl=li
#         li=i
#     elif i > s_largest:
#         s_largest=l[i]
#         si=i
# print(largest,li)
# print(s_largest,si)



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

  
# TCS question 
# rotate a list by k elements
# l=[1,2,3,4,5] #o/p= k=2,[4,5,1,2,3]
# k=2
# for i in range(k): 
#     last=l[-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=last
# print(l)

                                  # or

# for i in range(k):
#     for i in range(len(l)-1):
#         l[i],l[i+1]=l[i+1],l[i]
# print(l)




# assign all the 0s at the end of the list
# l=[0,1,0,3,12]
# j=0
# for i in range(len(l)):
#   if l[i]!=0:
#     l[i],l[j]=l[j],l[i]
#     j=j+1
# print(l)


# how to find duplicates and add in a list and remove it

        # arr = [nums[0]]

        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1]:
        #         arr.append(nums[i])


# vlist = [1,2,3,2,4,5,1]

# arr = [vlist[0]]

# for i in range(1, len(vlist)):
#     if vlist[i] != vlist[i-1]:
#         arr.append(vlist[i])

# print(arr)