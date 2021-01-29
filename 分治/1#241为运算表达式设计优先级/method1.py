# 分治算法三步走：
# 分解：按运算符分成左右两部分，分别求解
# 解决：实现一个递归函数，输入算式，返回算式解
# 合并：根据运算符合并左右两部分的解，得出最终解
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for idx, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[0:idx])
                right = self.diffWaysToCompute(input[idx+1:])
                for i in left:
                    for j in right:
                        if c is '+':
                            res.append(i + j)
                        elif c is '-':
                            res.append(i - j)
                        else:
                            res.append(i * j)
        return res







