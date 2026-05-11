class Solution:
    def customSortString(self, order: str, s: str) -> str:

        interm={}
        interm_s=''
        for i in s:
            if i in interm:
                interm[i]+=1
            else:
                interm[i]=1

        for i in order :
            if i in interm:
                interm_s+=i*interm[i]
                interm.pop(i)
            
        for i in interm:
            interm_s+=i*interm[i]
        return interm_s

        