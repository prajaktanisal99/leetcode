class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        # product map
        hash = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                key = nums[i] * nums[j]
                hash[key] = hash.get(key, 0) + 1
        
        res = 0
        for key, val in hash.items():
            if val > 1:
                res += (val * (val - 1) // 2) * 8

        return res