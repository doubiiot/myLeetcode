class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        mid = x // 2
        while True:
            if mid * mid < x:
                if (mid+1) * (mid+1) > x:
                    return mid
                else:
                    l = mid + 1
                    mid = (l + r) // 2
            elif mid * mid > x:
                r = mid - 1
                mid = (l + r) // 2
            else:
                return mid
