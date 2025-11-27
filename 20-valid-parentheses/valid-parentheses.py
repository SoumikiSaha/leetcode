class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # stack to store opening brackets
        mapping = {')': '(', '}': '{', ']': '['}  # closing → opening

        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop from stack if available, else assign dummy '#'
                top = stack.pop() if stack else '#'

                # If popped bracket is not the matching opening
                if mapping[char] != top:
                    return False

            else:
                # It's an opening bracket → push to stack
                stack.append(char)

        # Valid only if stack is empty
        return len(stack) == 0
