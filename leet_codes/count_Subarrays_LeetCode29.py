class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cont = 0
        aux = []
        i = 0 
        while i <= len(nums)-1:
            aux.append(nums[i])
            if len(aux) == 3:
                if 2*(aux[0] + aux[2]) == aux[1]:
                    cont += 1
                    aux = []
                    i -= 1
                    continue
                else:
                    aux = []
                    i -= 1
                    continue
            i += 1
        return cont