class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 not in arr:
            return False
        visited = [False]*len(arr)
        return self.dfs(arr, start, visited)
    
    def dfs(self, arr, start, visited):
        if arr[start] == 0:
            return True
        visited[start] = True
        for i in [start+arr[start], start-arr[start]]:
            if 0 <= i < len(arr) and not visited[i]:
                if self.dfs(arr, i, visited):
                    return True
        return False

