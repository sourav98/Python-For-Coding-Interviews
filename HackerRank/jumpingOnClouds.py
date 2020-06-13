def jumpingOnClouds(n,c):
    jumps=0
    i=0
    while(i<n-1):
        if c[i+2]!=1:
            jumps+=1
            i=i+2
        else:
            jumps+=1
            i=i+1
    return jumps
n=int(input())
c=list(map(int,input().rstrip().split()))

result=jumpingOnClouds(n,c)
print(result)

"""
Warm Up HackerRank Challenges

https://www.hackerrank.com/challenges/jumping-on-the-clouds

"""