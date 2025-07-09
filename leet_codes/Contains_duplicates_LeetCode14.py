class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        aux_set = set(nums)
        if len(aux_set) != len(nums):
            return True
        else:
            return False