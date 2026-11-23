class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        working = []
        working.append(asteroids.pop(0))
        while asteroids:
            working.append(asteroids.pop(0))
            while len(working) >= 2 and working[-2] > 0 and working[-1] < 0:
                a = working.pop()
                b = working.pop()
                if abs(a) > abs(b):
                    working.append(a)
                elif abs(b) > abs(a):
                    working.append(b)
                
        return working
            
        
             
        