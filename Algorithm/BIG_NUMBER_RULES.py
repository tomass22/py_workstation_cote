import sys # 시스템 클래스 불러옴

N,M,K= map(int, input().split()) 
    # N : # M : # K :
    # map : 순서쌍 만들어주는 함수 # 자료형을 정해줌 # input().split() 입력 받아서 나눠서 받는다 각각은 공백으로 구분한다. 

sum=0 
    # 변수

numlist= list(map(int, input().split()))
    # 리스트를 만들어주는데 순서쌍을 만들어서 넣어준다.

sortnumlist=sorted(numlist)
    # sort() : 정렬 default 값 : 오름차순

for i in range(1,M+1,1): # range(시작, 끝+1, 증감)
    if (i%(K+1)==0):
        sum+=sortnumlist[N-2]
    else:    
        sum+=sortnumlist[N-1]

print(sum)

#1 2 3 4 5 6 7 8


    