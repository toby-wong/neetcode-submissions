class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        
        prefix = 1
        for i in range(0, length):
            left[i] = prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(length-1, -1, -1):
            left[i] *= suffix 
            suffix *= nums[i]

        return left