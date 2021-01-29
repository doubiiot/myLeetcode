class Solution:
    def mySqrt(self, x: int) -> int:
        def get_sqrt(l, r):
            mid = (l+r) // 2
            if mid * mid < x:
                if (mid+1) * (mid+1) > x:
                    return mid
                return get_sqrt(mid+1, r)
            elif mid * mid > x:
                return get_sqrt(l, mid-1)
            else:
                return mid
        return get_sqrt(0,x)
