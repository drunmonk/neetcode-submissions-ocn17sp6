class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_=0
        cache={}
        for i in range(len(s)-1):
            if i+1 <len(s):
               if (s[i],s[i+1]) in cache:
                    sum_=sum_+ cache[(s[i],s[i+1])]
               else:
                 interm_sum=abs(ord(s[i])-ord(s[i+1]))
                 sum_ = sum_+interm_sum
                 cache[(s[i],s[i+1])]=interm_sum
            
        return sum_
        