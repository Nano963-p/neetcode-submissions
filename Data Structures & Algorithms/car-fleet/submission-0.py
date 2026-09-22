class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        t = list(zip(position,speed))
        s = sorted(t)
        while(len(s) != 0):
            diff = target - s[-1][0]
            time = diff / s[-1][1]
            if len(res) == 0:
                res.append(time)
                
            if time <= res[-1]:
                s.pop()
                continue
            else:
                res.append(time)
            s.pop()

        return(len(res))