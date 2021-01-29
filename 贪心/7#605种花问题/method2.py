class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        num = 0
        for i in range(length):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                num += 1
                flowerbed[i] = 1
            if num >= n:
                return True
        return False
#O(N) O(1)
