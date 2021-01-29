class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if length == 1 and flowerbed[0] == 0 and n <= 1:
            return True
        elif length == 1 and flowerbed[0] == 0 and n > 1:
            return False
        num = 0
        for i in range(length):
            if flowerbed[i] == 0:
                if i == 0:
                    if i+1 < length and not flowerbed[i+1]:
                        num += 1
                        flowerbed[i] = 1
                elif i == length - 1:
                    if i-1 >= 0 and not flowerbed[i-1]:
                        num += 1
                        flowerbed[i] = 1
                else:
                    if i+1 < length and i-1 >= 0 and not flowerbed[i+1] and not flowerbed[i-1]:
                        num += 1
                        flowerbed[i] = 1
        return num >= n

