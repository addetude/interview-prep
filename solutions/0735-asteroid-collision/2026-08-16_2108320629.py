class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        working = []
        n = len(asteroids)
        working.append(asteroids[0])
        i = 1
        while i < n:
            working.append(asteroids[i])
            i += 1
            while len(working) >= 2 and working[-2] > 0 and working[-1] < 0:
                a = working.pop()
                b = working.pop()
                if abs(a) > abs(b):
                    working.append(a)
                elif abs(b) > abs(a):
                    working.append(b)
                
        return working
            
        
             
        