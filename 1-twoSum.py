class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev = dict()
        for ind,no in enumerate(nums):
            if target-no not in prev:
                prev[no]=ind
                continue
            return [ind, prev[target-no]]