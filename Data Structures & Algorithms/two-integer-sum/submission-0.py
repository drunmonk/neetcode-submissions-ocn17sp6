class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        interm={}

        for i in range(len(nums)):
            rem=target-nums[i]

            if rem in interm:
                return [interm[rem],i]
            else:
                interm[nums[i]]=i