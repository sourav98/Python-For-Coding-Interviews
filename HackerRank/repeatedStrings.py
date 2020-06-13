def repeatedString(s, n):
    n1=n//len(s)
    x1=s.count('a')
    c1=x1*n1
    c2=s[:n%len(s)].count('a')
    return c1+c2

s=input()
n=int(input())

result = repeatedString(s,n)
print(result)


"""
Warm Up HackerRank Challenges

https://www.hackerrank.com/challenges/repeated-string

"""