class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        if len(nums1)%2==1:
            return nums1[floor(len(nums1)/2)]
        else:
            size_by_2 = len(nums1)//2  
            return (nums1[size_by_2]+nums1[size_by_2-1])/2
            
