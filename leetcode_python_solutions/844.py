class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s) - 1, len(t) - 1
        while p1 >= 0 or p2 >= 0:
            c1, c2 = "", ""
            if p1 >= 0:
                c1, p1 = self.get_c(s, p1)
            if p2 >= 0:
                c2, p2 = self.get_c(t, p2)
            if c1 != c2:
                return False
        return True

    def get_c(self, string, p):
        count = 0
        c = ""
        while p >= 0 and not c:
            if string[p] == "#":
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    c = string[p]
            p -= 1
        return c, p
