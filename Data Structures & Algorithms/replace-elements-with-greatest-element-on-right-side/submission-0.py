class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)):
            j=i+1
            if  j< len(arr):
              arr[i]=max(arr[j:])
        arr[-1]=-1
        return arr
        