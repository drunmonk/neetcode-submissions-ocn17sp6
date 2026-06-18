class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache={}

        for i in range(len(nums)):
            if nums[i] in cache and abs(cache[nums[i]]-i)<=k:
                return True
            else:
                cache[nums[i]]=i
        return False
         





        