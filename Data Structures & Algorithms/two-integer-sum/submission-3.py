class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for k,v in enumerate(nums):
            diff = target - v
            if diff in numsMap:
                return sorted([k, numsMap[diff]])
            numsMap[v] = k

