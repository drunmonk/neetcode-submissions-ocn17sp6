class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_=arr[-1]
        temp=0

        for i in range(-1,-len(arr)-1,-1):
            temp=arr[i]
            arr[i]=max_
            max_=max(max_,temp)
        arr[-1]=-1
        return arr


        