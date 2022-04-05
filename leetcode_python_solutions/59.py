class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[None]*n for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = 0, 0
        d = 0
        for num in range(1, n**2+1):
            mat[i][j] = num
            x = i + direction[d%4][0]
            y = j + direction[d%4][1]
            if x == n or x == -1 or y == n or y == -1 or mat[x][y] != None:
                d += 1
            i = i + direction[d%4][0]
            j = j + direction[d%4][1]
        return mat
    

