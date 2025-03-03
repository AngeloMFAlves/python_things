class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_total = nums1 + nums2
        sorted_list = sorted(list_total)
        if len(sorted_list)%2 == 0:
            median = ((sorted_list[(len(sorted_list)//2)-1]+sorted_list[len(sorted_list)//2]))/2
            return float(median)
        if len(sorted_list)%2 != 0:
            for i in range(len(sorted_list)):
                if len(sorted_list[:i]) == len(sorted_list[i+1:]):
                    median = sorted_list[i]
                    return float(median)