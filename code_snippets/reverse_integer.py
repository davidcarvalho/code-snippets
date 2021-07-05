class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            negative = True
        else:
            negative = False
        rev = 0
        if x == 0:
            return 0
        else:
            while x > 0:
                rev = (rev * 10) + (x % 10)
                x = x // 10
            if negative:
                rev = -rev
            return rev


sol = Solution()
print(sol.reverse(-123456789))
