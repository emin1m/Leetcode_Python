## First solution include double for loop, this is O(N^2) complexicty
# which causes higher memory usage

class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return False


solution = Solution()
print(solution.twoSum([4,5,6],target=10))

print(solution.twoSum(nums = [3,4,5,6], target = 7))

print(solution.twoSum(nums = [5,5], target = 10))


# Second solution include only one for loop, O(N) complexicty
# Code works more efficient
class Solution2:
    def twoSum(self,nums:list[int], target:int) -> list[int]:
        
        num_dict = {}
        for i,num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target-num],i]
            else:
                num_dict[num] = i
        
solution2 = Solution2()

print(solution2.twoSum(nums = [3,4,5,6], target = 7))





    

        





        

        
        
