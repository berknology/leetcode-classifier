class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = collections.deque([(amount, 0)])
        visited = set()
        while queue:
            val, step = queue.popleft()
            if val == 0:
                return step
            for coin in coins:
                if val - coin < 0 or val-coin in visited:
                    continue
                visited.add(val-coin)
                queue.append((val-coin, step+1))
        return -1

            
