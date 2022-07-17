import sys
import heapq
n=int(sys.stdin.readline())
heap=[]
for i in range(n):
    ans=int(sys.stdin.readline())
    if ans!=0:
        heapq.heappush(heap,(abs(ans),ans))
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])