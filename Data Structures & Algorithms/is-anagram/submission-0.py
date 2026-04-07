class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        org={}
        
        if len(s)!=len(t):
            return False
        for i in s:
            org[i] = org.get(i, 0) + 1
        
        for i in t:
            if i in org :
                if org[i] ==0:
                    return False
                org[i]-=1
            else:
              return False
        return True
                    