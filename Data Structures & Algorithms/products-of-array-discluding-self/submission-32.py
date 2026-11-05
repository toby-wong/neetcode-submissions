class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length
        curr = 1

        for i in range(1, length):
            left[i] = nums[i-1] * left[i-1]
            
        for i in range(length - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        return [i*j for i,j in zip(left,right)]