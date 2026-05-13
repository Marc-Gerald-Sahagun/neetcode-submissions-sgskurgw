class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        occur = {}

        # creates the occur dict
        for num in nums:
            occur[num] = occur.get(num, 0) + 1

        buckets = [[] for __ in range(len(nums) + 1)]

        for num, count in occur.items():
            buckets[count].append(num)

        result = []

        for bucket in range(len(buckets)-1, 0, -1):
            for num in buckets[bucket]:
                result.append(num)
                if len(result) == k:
                    return result
                    


        