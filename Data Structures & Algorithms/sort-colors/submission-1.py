class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s={0:0,1:0,2:0}
        k=0
        for i in nums:
            if i in s :
                s[i]+=1
        
        for i in s:
            for _ in range(s[i]):
                nums[k]=i
                k+=1
        
