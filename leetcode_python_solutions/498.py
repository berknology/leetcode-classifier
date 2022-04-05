class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        hash_table = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                hash_table[i+j].append(matrix[i][j])
        ans = []
        for key in hash_table:
            if key %2 == 0:
                ans.extend(hash_table[key][::-1])
            else:
                ans.extend(hash_table[key])
        return ans
    
"""
0: 1
1: 2, 4
2: 3, 5, 7
3: 6, 8
4: 9
"""
        

