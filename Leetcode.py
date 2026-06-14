#2341  Make Array Zero by Subtracting Equal Amounts
# nums = [1,5,0,3,5]
# l = []

# for i in nums:
#     if i in l or i == 0:
#         continue
#     else:
#         l.append(i)

# print(l)



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


#2206 divide array into two equal parts
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


#2357
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


# 2293
        # while len(nums) >1:
        #     newNums=[]
        #     for i in range(len(nums)//2):
        #         if i%2==0:
        #             newNums.append(min(nums[2 * i], nums[2 * i + 1]))
        #         else :
        #             newNums.append( max(nums[2 * i], nums[2 * i + 1]))
        #     nums =newNums


 #2341
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
#             leftover += i % 2


#2160 Minimum Sum of Four Digit Number After Splitting Digits
# nums=6779
# digit=sorted(str(nums))
# new1=digit[0]+digit[2]
# new2=digit[1]+digit[3]

# print(int(new1) + int(new2))


#2164
# class Solution:
#     def sortEvenOdd(self, nums: List[int]) -> List[int]:
#         even=[]
#         odd=[]
#         for i in range(len(nums)):
#             if i%2==0:
#                 even.append(nums[i]) 
                
#             else:
#                 odd.append(nums[i])
                
#         even.sort()
#         odd.sort(reverse=True)
         

#         e = 0
#         o = 0

        
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 nums[i] = even[e]
#                 e += 1
#             else:
#                 nums[i] = odd[o]
#                 o += 1

#         return nums
      
    

            
#2078
# class Solution:
#     def maxDistance(self, colors: List[int]) -> int:
#         ans=0
#         for i in range(len(colors)):
#             for j in range(len(colors)-1,-1,-1):
#                 if colors[i] != colors[j]:
#                     ans = max(ans, abs(i-j))
#                 else:
#                     continue
#         return (ans)



           
# Q1732 Find the Highest altitude 
# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         altitude=0
#         max_altitude=0
#         for i in gain:
#             altitude+=i
#             max_altitude=max(max_altitude,altitude)
#         return(max_altitude)

        



#Q2037
# class Solution:
#     def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
#         seats.sort()
#         students.sort()
#         moves=0
#         for i in range(len(seats)):
#             moves=moves+abs(seats[i]-students[i])
#         return moves



#Q2399. Check distances Between same letters
# class Solution:
#     def checkDistances(self, s: str, distance: List[int]) -> bool:
#         seen = {}

#         for i, ch in enumerate(s):
#             if ch in seen:
#                 gap = i - seen[ch] - 1
#                 if gap != distance[ord(ch) - ord('a')]:
#                     return False
#             else:
#                 seen[ch] = i

#         return True



# Q2309. Greatest English Letter in Upper and Lower Case
# class Solution:
#     def greatestLetter(self, s: str) -> str:
#         for ch in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
#             if ch.lower() in s and ch.upper() in s:
#                 return ch
#         return ""


#Q58. Length of Last Word
# word=s.strip().split()
# return (s.word([-1]))
# strip= Remove extra spaces from the beginning and end using strip().
# split=Split the string into words using split()