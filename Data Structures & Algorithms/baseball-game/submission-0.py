class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ls = []
        for i in operations:
            try:
                ls.append(int(i))
            except ValueError:
                if i == '+':
                    ls.append(ls[-2] + ls[-1])
                elif i == 'C':
                    ls.pop()
                elif i == 'D':
                    ls.append((ls[-1] * 2))
        num = 0 
        for i in range(len(ls)):
            num += ls.pop()
        return num
        