#Anagram problem
#One can solve this problem very easy with using built-in function (sorts)
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_word = {}
        
        for letter in s:
            if letter not in dict_word:
                dict_word[letter] = 1
            else:
                dict_word[letter] +=1
        
        for letter in t:
            if letter not in dict_word:
                return False
            else:
                dict_word[letter] -=1
            
        for num in dict_word.values():
            if num != 0:
                return False
        return True 
    
solution = Solution()

print(solution.isAnagram("racecar","carrace"))
print(solution.isAnagram("carrra","arrac"))
        
