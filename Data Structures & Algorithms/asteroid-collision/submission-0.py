class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for momentum in asteroids:
            while stack and stack[-1] > 0 > momentum:
                if -momentum == stack[-1]:
                    stack.pop()
                    momentum = 0
                elif -momentum > stack[-1]:
                    stack.pop()
                elif -momentum < stack[-1]:
                    momentum = 0
            if momentum:
                stack.append(momentum)
        return stack