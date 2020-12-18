class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pa = 0
        pb = 0
        ans = []
        while pa < len(A) and pb < len(B):
            if A[pa][1] < B[pb][0]:
                pa += 1
            elif B[pb][1] < A[pa][0]:
                pb += 1
            else:
                ans.append([max(A[pa][0], B[pb][0]), min(A[pa][1], B[pb][1])])
                if A[pa][1] <= B[pb][1]:
                    pa += 1
                else:
                    pb += 1
        return ans
    
            
            
        
"""
xxxx
      xxxx


       xxxx
xxx
    

      xxxxxxxxx
    xxx

"""
