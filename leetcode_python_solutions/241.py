class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        ans = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if c == "*":
                            ans.append(l*r)
                        elif c == '+':
                            ans.append(l+r)
                        else:
                            ans.append(l-r)
        return ans
