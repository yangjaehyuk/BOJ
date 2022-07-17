import sys
import heapq
x=int(sys.stdin.readline())
heap=[]
for i in range(x):
    ans=int(sys.stdin.readline())
    if ans!=0:
        heapq.heappush(heap,ans)
    else:
        if len(heap)>0:
            print(heapq.heappop(heap))
        else:
            print(0)