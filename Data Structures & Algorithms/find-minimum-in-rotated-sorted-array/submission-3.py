class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        length = len(nums)

        start, end = 0, length-1

        while start < end:
            half = (end-start)//2 + start
            if nums[half] > nums[half+1]:
                return nums[half+1]
            if nums[half] > nums[end]:
                start = half
            else:
                end = half