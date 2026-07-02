class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        s=[]

        for i in logs:

            if i=='../':
                if s:
                    s.pop()
            elif i!='./':
                s.append(i)
        return len(s)
        
        