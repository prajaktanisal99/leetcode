class Solution:
    def check(self, nums: List[int]) -> bool:
        
        drops = 0
        n = len(nums)
        for i in range(n):
            if nums[i % n] > nums[(i + 1) % n]:
                drops += 1
                if drops == 2:
                    return False

        return True