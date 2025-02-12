class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort the given list of numbers
        sorted_nums = sorted(nums)
        
        # The majority element always appears more than ⌊n/2⌋ times,
        # so after sorting, it will always be at index len(nums) // 2
        return sorted_nums[len(nums) // 2]
