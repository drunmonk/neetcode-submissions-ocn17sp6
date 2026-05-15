class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrom(i,l):
            while i<l:
                if s[i] != s[l]:
                    return False
                i+=1
                l-=1
            return True
        
        i=0
        l=len(s)-1

        while i <l:
            if s[i] != s[l]:
                return (is_palindrom(i+1,l) or is_palindrom(i,l-1))
            i+=1
            l-=1
        return True

        