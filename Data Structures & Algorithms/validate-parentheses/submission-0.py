class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in pairs:  # checking only opening
                stack.append(char)
            else:  
                if not stack: # if stack empty
                    return False
                last_opening = stack.pop()
                expected_closing = pairs[last_opening]
                if expected_closing != char:
                    return False

    #basically you pop the last opening which is like [, { etc
    #then expected closing u get the matching on pairs so for [ its : ]
    # then is it the char ur looking at rn 
        
        # If stack is empty, all brackets were matched properly
        return len(stack) == 0
