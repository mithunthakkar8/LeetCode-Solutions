class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num==target or num>target:
                return i
                break
            elif i==len(nums)-1:
                return i+1
                break
