from typing import List, Dict


class Solution:
    """
    TC - O(n)
    SC - O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map: Dict[int, int] = dict()

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in map:
                return [i, map[compliment]] if map[compliment] > i else [map[compliment], i]

            map[nums[i]] = i

        return []