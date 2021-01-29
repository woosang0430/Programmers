import heapq

def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    
    h = []
    for i in d:
        heapq.heappush(h, i)
        
    ret = 0
    for i in range(len(d)):
        ret += heapq.heappop(h)
        if ret > budget:
            return i
