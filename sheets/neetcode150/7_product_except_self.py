class Solution:
    """
    Naive
    TC - O(n)
    SC - O(n)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        postfix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        res = [1] * n
        for i in range(n):
            res[i] = prefix[i] * postfix[i]

        return res


class Solution:
    """
    Optimal
    TC - O(n)
    SC - O(1) auxiliary space : O(n) res including array
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res