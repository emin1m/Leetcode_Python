# Level is easy
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: list[int]) ->bool:
        nums_2 = [] # empty list

        for num in nums:

            if num in nums_2:
                return True
            else:
                nums_2.append(num) # if the num is not in nums_2, append to the list 
        return False
    

solution = Solution()

print(solution.hasDuplicate(nums = [1, 2, 3, 3])) # True

print(solution.hasDuplicate([1, 2, 3, 4])) # False
