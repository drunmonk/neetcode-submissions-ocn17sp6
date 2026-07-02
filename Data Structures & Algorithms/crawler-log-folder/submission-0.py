class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        a={
            "./":0,
            "../":-1
        }
        s=0
        for i in logs:
            if i not in a:
                s+=1
            else:
                if s>0:
                    s+=a[i]
        
        return s
