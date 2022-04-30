import sys

N,M,K= map(int, input().split())
sum=0
numlist= list(map(int, input().split()))
sortnumlist=sorted(numlist)
for i in range(1,M+1,1):
    if (i%K==0):
        sum+=sortnumlist[N-2]
    else:    
        sum+=sortnumlist[N-1]

print(sum)


    


