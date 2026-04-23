class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l_=0
        i=len(s)-1
        while s[i] ==' ':
               i-=1
        while  i>=0 and s[i] !=' ' :
            l_+=1
            i-=1
        
        return l_
                
            

        

             