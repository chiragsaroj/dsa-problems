from typing import List

class Solution:
    """ 
    Brute 
    TC - O(n^2)
    SC - O(1)
    """
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True

        return False


class Solution:
    """ 
    Better 
    TC - O(n log n)
    SC - O(n) : It depends on language you use.
    """
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False


class Solution:
    """ 
    Optimized 
    TC - O(n)
    SC - O(n)
    """

    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False