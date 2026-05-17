class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if stack[-1] < -ast:
                    stack.pop()   # top explodes
                    continue
                elif stack[-1] == -ast:
                    stack.pop()   # both explode
                break
            else:
                stack.append(ast)
    
        return stack

        