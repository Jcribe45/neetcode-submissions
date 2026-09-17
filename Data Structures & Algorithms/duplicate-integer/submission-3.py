class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        num_list = []
        for i in range(len(nums)):
            if nums[i] in num_list:
                return True
            num_list.append(nums[i])
        return False