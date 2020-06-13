def sockMerchant(n,ar):
    pairs=0
    colors=set(ar)
    for color in colors:
        pairs+=ar.count(color)//2
    return pairs

n= int(input())
ar=list(map(int,input().rstrip().split()))

result=sockMerchant(n,ar)
print(result)

"""
Warm Up HackerRank Challenges

https://www.hackerrank.com/challenges/sock-merchant 

"""