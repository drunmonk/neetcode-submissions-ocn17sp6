class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l_=0
        L_f=0
        for i in nums:
            if i ==0:
                L_f=max(l_,L_f)
                l_=0
            else:
                l_+=1
        return max(l_,L_f)