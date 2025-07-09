class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ways = 0
        prefix = []
        prefix.append(nums[0])
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1] + nums[i])
        sum_total_array = prefix[len(prefix) - 1]
        for i in range(len(prefix)-1):
            sum_left = prefix[i]
            sum_right = sum_total_array - sum_left
            if sum_left >= sum_right:
                ways +=1
        return ways