class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_i,idx=float('-inf'),0
        for i in range(len(arr)):
            if idx ==i and i < len(arr)-1:
                max_i=max(arr[i+1:])
                idx=arr.index(max_i)
            arr[i] =max_i
        arr[-1]=-1
        return arr
        