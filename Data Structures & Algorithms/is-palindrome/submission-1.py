class Solution:
    def isalphnum(self,x:str) -> bool:
        return ((ord('A')<=ord(x)<=ord('Z')) or 
        (ord('a')<=ord(x)<=ord('z')) or
        (ord('0')<=ord(x)<=ord('9')))


    def isPalindrome(self, s: str) -> bool:
        
        i=0
        j=len(s)-1


        while i <j:

            while i<j and not self.isalphnum(s[i]):
                i+=1
            while j>i  and not self.isalphnum(s[j]):
                j-=1
            
            if s[i].upper() != s[j].upper():
                return False
            i+=1
            j-=1
            
        
        return True


            


