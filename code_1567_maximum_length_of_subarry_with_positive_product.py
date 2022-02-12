class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        neg = int(nums[0] < 0)
        pos = int(nums[0] > 0)
        ans = pos
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)
        return ans

