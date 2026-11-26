import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mp = {}
        for p in points:
            d = p[0]**2+p[1]**2 
            if d in mp.keys():
                mp[d].append(p)
            else:
                mp[d] = [p]
        topK = heapq.nsmallest(k, mp.keys())
        r = []
        for i in topK:
            r += mp[i]
            if len(r) >= k:
                break
        return r