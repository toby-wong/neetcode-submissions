class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # Stores seen numbers as keys and their indices as values
        seen = {}
        
        for i, num in enumerate(numbers):
            complement = target - num
            
            # If the complement is already in the hash map, we found our pair
            if complement in seen:
                return [seen[complement]+1, i+1]
                
            # Otherwise, track the current number and its index
            seen[num] = i