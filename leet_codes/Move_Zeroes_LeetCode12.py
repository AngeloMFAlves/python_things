class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        list_aux = [i for i in nums]
        for i in nums:
            if i == 0:
                nums.append(0)
                nums.remove(i)
        