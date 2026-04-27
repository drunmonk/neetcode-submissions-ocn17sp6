class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        interm=strs[0]
       
        for i in range(len(strs)):
            j=0
            while j < min(len(interm),len(strs[i])):
                if interm[j]!=strs[i][j]:
                    break
                j+=1
            interm=interm[:j]
        
        return interm



        

        

        