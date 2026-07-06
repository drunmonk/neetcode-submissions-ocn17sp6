class Solution:
    def calPoints(self, operations: List[str]) -> int:

        s_=[]

        for i in operations:

            if i =='+':
                s_.append(s_[-1]+s_[-2])
            elif i=='C':
                s_.pop()
            elif i=='D':
                s_.append(s_[-1]*2)
            else:
                s_.append(int(i))
        
        return sum(s_)

        