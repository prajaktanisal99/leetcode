class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find longest prefix
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return

        # find smallest greater number than nums[index] from end
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]

        # sort the array after index in ascending order or just reverse it
        nums[index+1:] = reversed(nums[index+1:])
        