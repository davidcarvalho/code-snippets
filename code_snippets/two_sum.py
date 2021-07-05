class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # for idx, i in enumerate(nums):
        #     x = i
        #     y = target - x
        #     s = set(nums[idx+1:])
        #     if y in s:
        #         if x == y:
        #             temp = nums.index(x)
        #             return [idx, nums[temp + 1:].index(y) + temp + 1]
        #         else:
        #             return [idx, nums.index(y)]

        d = {}
        for idx, i in enumerate(nums):
            y = target - i
            if y not in d:
                d[i] = idx
            else:
                return [d[y], idx]


sol = Solution()
print(sol.twoSum([3, 2, 4], 6))
