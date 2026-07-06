class Solution:
    def calPoints(self, operations: List[str]) -> int:

        s_=[]
        res=0

        for i in operations:

            if i =='+':
                res+=(s_[-1]+s_[-2])
                s_.append(s_[-1]+s_[-2])
                
            elif i=='C':
                res-=s_.pop()
            elif i=='D':
                res+=(s_[-1]*2)
                s_.append(s_[-1]*2)
                
            else:
                res+=int(i)
                s_.append(int(i))
                
        
        return res

        