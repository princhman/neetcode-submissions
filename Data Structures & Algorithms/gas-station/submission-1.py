class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        cache = {} # start: (finish, fuel)
        def test(start: int) -> bool:
            tank = gas[start] - cost[start]
            i = (start + 1) % len(gas)
            while tank >= 0 and i != start:
                # if i in cache:
                #     tank += cache[i][1]
                #     i = cache[i][0]
                # else:
                tank += gas[i] - cost[i]
                i = (i + 1) % len(gas)
            if i == start and tank >= 0:
                return True
            # else:
                # cache[start] = (i, tank)
        for k in range(len(gas)-1, -1, -1):
            if test(k):
                return k
        return -1

