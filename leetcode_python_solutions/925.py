class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]: return False
        p1 = p2 = 1
        while p1 < len(name) and p2 < len(typed):
            if name[p1] == typed[p2]:
                p1 += 1
            else:
                if typed[p2] != typed[p2-1]:
                    return False
            p2 += 1
        while p2 < len(typed):
            if typed[p2] != typed[p2-1]:
                return False
            p2 += 1
        return p1 == len(name)
