class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack
        # pop the values 
        # check if value is an interger add it to score
        # check if value is C remove the 
        stack = []
        for i in range(len(operations)):
            if operations[i] == '+':
                stack.append(int(stack[-2]) + int(stack[-1]))
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                stack.append(2 * int(stack[-1]))
            else:
                stack.append(int(operations[i]))

        return sum(stack)