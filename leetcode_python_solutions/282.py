class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        self.ans = []
        self.backtrack(num, target, index=0, path='', res=0, pre=0)
        return self.ans
    
    def backtrack(self, num, target, index, path, res, pre):
        if index == len(num) and res == target:
            self.ans.append(path)
            return
        for i in range(index, len(num)):
            sub_str = num[index:i+1]
            if len(sub_str) > 1 and sub_str[0] == '0':
                break
            if len(path) == 0:
                self.backtrack(num, target, i+1, sub_str, int(sub_str), int(sub_str))
            else:
                self.backtrack(num, target, i+1, path+"+"+sub_str, res+int(sub_str), +int(sub_str))
                self.backtrack(num, target, i+1, path+"-"+sub_str, res-int(sub_str), -int(sub_str))
                self.backtrack(num, target, i+1, path+"*"+sub_str, res-pre+int(sub_str)*pre, int(sub_str)*pre)
