import sys
import heapq
n=int(sys.stdin.readline())
heap=[]
for i in range(n):
    ans=int(sys.stdin.readline())
    ans=-1*ans
    if ans!=0:
        heapq.heappush(heap,ans)
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)*-1)