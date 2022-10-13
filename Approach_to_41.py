class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        f=0
        while i<n:
            x=nums[i]-1
            if x==i:
                i+=1
            elif x<0 or x>=n:
                i+=1
            else:
                b=nums[x]
                nums[i],nums[x]=b,x+1
                if b==x+1:
                    i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1 
