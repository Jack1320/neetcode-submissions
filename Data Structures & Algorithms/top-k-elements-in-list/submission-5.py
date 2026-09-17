class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        # bucket sort
        # which we use since the frequency of nums[i] is in {1,2,...,len(nums)}

        buckets = [[] for _ in range(len(nums))]
        for i in seen:
            buckets[seen[i] - 1].append(i)

        # read buckets backwards until you fill an answer array
        answer = []

        for i in range(len(nums) -1, -1, -1):
            if len(answer) != k:
                answer += buckets[i]
        return answer

