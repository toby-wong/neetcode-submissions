class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print({i:nums.count(i) for i in nums})
        # counts = {i:nums.count(i) for i in nums}
        # print(Counter(counts))
        # res = []
        # for i in range(k):
        #     res.append(Counter(counts).first())
        #     Counter(counts).pop()

        # counts = list(zip(Counter(nums).sort().keys(), Counter(nums).values()))
        # print(counts)
        # return [counts.values[i] for i in range(k)]

        return [i for i,j in Counter(nums).most_common(k)]