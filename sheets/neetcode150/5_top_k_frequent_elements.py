class Solution:
    """
    Naive
    TC - O(n + mlog m)
    SC - O(m)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_map = dict(
            sorted(freq_map.items(), key=lambda item: item[1], reverse=True)
        )

        res = []
        for num, freq in sorted_map.items():
            if len(res) == k:
                break

            res.append(num)

        return res



class Solution:
    """
    Optimized
    TC - O(n)
    SC - O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        res = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)

            if len(res) == k:
                return res

        return res