class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for i in range(len(s)):
            if s[i].isalnum() == True:
                a += s[i]
        a = a.casefold()
        if a[::-1] == a:
            return True
        else:
            return False
            
        

   

        
        