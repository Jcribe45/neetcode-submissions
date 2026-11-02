class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        length = len(nums)

        def bin_min(start, end):
            half = (end-start)//2 + start
            if nums[half] > nums[half+1]:
                return nums[half+1]
            else:
                if nums[half] > nums[end]:
                    return bin_min(half,end)
                else:
                    return bin_min(start,half)

        return bin_min(0,length-1)