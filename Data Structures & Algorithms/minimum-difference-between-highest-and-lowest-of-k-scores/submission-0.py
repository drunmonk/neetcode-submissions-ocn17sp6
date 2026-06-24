class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        

        nums.sort()

        i=0
        j=k-1
        min_diff=float("inf")
        while j<len(nums):
          min_diff=min(min_diff,nums[j]-nums[i])  
          i+=1
          j+=1
        return min_diff
