class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}
        
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        buckets = [[] for __ in range(len(nums) + 1)]

        for num, count in seen.items():
            buckets[count].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result