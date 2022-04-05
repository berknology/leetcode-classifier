class Solution:
    def numTrees(self, n: int) -> int:
        return self.num_bst(1, n, dict())
        
    def num_bst(self, start, end, memo):
        if start >= end:
            return 1
        if (end-start) in memo:
            return memo[end-start]
        ans = 0
        for index in range(start, end+1):
            left = self.num_bst(start, index-1, memo)
            right = self.num_bst(index+1, end, memo)
            ans += left*right
        memo[end-start] = ans
        return ans


"""
BST
[1, 2, 3]


start   0
end     2
index   0 

index in  range(start, end+1)

left [start:index]

right [index+1:]

divide and conquer


"""
