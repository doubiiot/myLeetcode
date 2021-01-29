class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n))+1)]
        queue = {n}
        level = 0
        while queue:
            level += 1
            new_queue = set()
            for cur in queue:
                for num in square_nums:
                    if cur == num:
                        return level
                    elif cur < num:
                        break
                    else:
                        new_queue.add(cur-num)
            queue = new_queue
#O(n ^ (h/2)) O(n ^ (h/2))
