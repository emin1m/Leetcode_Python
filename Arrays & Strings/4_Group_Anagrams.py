
from collections import defaultdict # her yeni key  için manuel olarak bir başlangıç value atamanıza gerek kalmamasıdır. 
class Solution:
    def groupAnagrams(self,strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # creates array with 0, 26's elements from a to z

            for c in s:
                count[ord(c) - ord("a")] +=1 # ord converts to ASCII num
            
            res[tuple(count)].append(s) ## need tuple cuz, it can take 2 key value but list can not take more than 1 
        
        return res.values()


solution = Solution()

print(solution.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))


print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))






### TUPLE EXAMPLE

# Creating a dictionary with tuples as keys
tuple_dict = {
    (1, 2): "a",
    (3, 4): "b"
}

# Accessing values using tuple keys
print(tuple_dict[(1, 2)])  # Output: "a"
print(tuple_dict[(3, 4)])  # Output: "b"
