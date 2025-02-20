class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y[::-1] == y:
            return True
        else:
            return False
        
        
solution = Solution()
ex1 = 121
ex2 = -121
result = solution.isPalindrome(ex1)
print(result)
result = solution.isPalindrome(ex2)    
print(result)
