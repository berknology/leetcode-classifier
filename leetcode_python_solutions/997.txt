class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_deg = [0]*N
        out_deg = [0]*N
        for pair in trust:
            out_deg[pair[0]-1] += 1
            in_deg[pair[1]-1] += 1
        for i in range(N):
            if in_deg[i] == N-1 and out_deg[i] == 0:
                return i+1
        return -1
