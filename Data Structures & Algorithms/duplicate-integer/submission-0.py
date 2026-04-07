class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        org=set()

        for i in nums:
            if i in org:
                return True
            org.add(i)

        return False


        