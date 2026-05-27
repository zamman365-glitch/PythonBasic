# d1={1:10,2:30,3:30}
# d1={4:40,5:50,6:60}
# for i in d1:
#     print(d1[i])

# d1={1:10,2:30,3:30}
# d2={4:40,5:50,6:60}
 
# for i in d2:
#     d1[i]=d2[i]
# print(d1)


# if dict having two same keys
# d1={1:10,2:30,3:30}
# d2={3:40,5:50,6:60}

# for i in d2:
#     if i in d1.keys():
#         d1[i]=d1[i] + d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)


# l=[1,1,1,2,2,2,3,4,5,5,5,5,6,6,6]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d[2])


#2206 leetcode
# l=[3,2,3,2,2,2]
# d={}

# for i in l:
#     if i in d:
#         d[i] +=1
#     else:
#         d[i]=1

# for i in d.values():
#     if i%2!=0:
#         print("not pair")
#     else:
#         print("pair")

# #2341
#         l=[3,2,3,2,2,2] 
#         d = {}

#         for i in l:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1

#         pairs = 0
#         leftover = 0

#         for i in d.values():
#             pairs += i // 2      # pairs
#             leftover += i % 2    # leftovers


# 2293
        # while len(nums) >1:
        #     newNums=[]
        #     for i in range(len(nums)//2):
        #         if i%2==0:
        #             newNums.append(min(nums[2 * i], nums[2 * i + 1]))
        #         else :
        #             newNums.append( max(nums[2 * i], nums[2 * i + 1]))
        #     nums =newNums


# #2357
# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         #Task 1 create a new list but dont 0 and repeated element
#         l=[]
#         for i in nums:
#             if i in l:
#                 continue
#             elif i==0:
#                 continue
#             else:
#                 l.append(i)
        
#         # task 2 return the length of the list back to leetcode
#         return len(l)
    


# # divide array into two equal parts
# l=[1,2,3,4,3,4,2,1,6]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d.values():
#     if i%2!=0:
#         print("not pairs")
#     else :
#         print("pairs")


# # max number of pairs in array
# l=[1,2,3,4,3,4,2,1,6]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# pairs=0
# leftover=0
# for i in d.values():
#     pairs =pairs+i//2 # pairs
#     leftover=leftover + i%2 # pairs
# print(f"pairs element = {pairs}")
# print(f"leftovers element = {leftover}")

#2341  Make Array Zero by Subtracting Equal Amounts
# nums = [1,5,0,3,5]
# l = []

# for i in nums:
#     if i in l or i == 0:
#         continue
#     else:
#         l.append(i)

# print(l)
       
