class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        l=0
        r=len(nums)-1
        res=[0]*(r+1)
        p=len(nums)-1
        while l<=r:
           
            if nums[l]*nums[l] < nums[r]*nums[r]:
                res[p]=(nums[r]**2)
                r-=1
            else:
                res[p]=(nums[l]**2)
                l+=1
            p-=1
        return res