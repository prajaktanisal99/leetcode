class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket Sort - 2 Pass solution
        # 2 Pointer - Single pass solution
        # left, right, and current

        current = 0
        left = 0
        right = len(nums) - 1

        while current <= right:
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1 
            if nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
                current -= 1

            current += 1