class Solution:
    def calPoints(self, operations: List[str]) -> int:

        s_=[]
        res=0

        for i in operations:

            if i =='+':
                t=(s_[-1]+s_[-2])
                s_.append(t)
                res+=t
                
            elif i=='D':
                t=(s_[-1]*2)
                s_.append(t)
                res+=t

            elif i=='C':
                res-=s_.pop()
            
                
            else:
                t=int(i)
                s_.append(t)
                res+=t
                
        
        return res

        