a=int(input())
if a<=2000: ans = 100
else: ans=100+(a-2000+499)//500*5

print(ans)


a = list(map(int,input().split()))
print( sum(a)-a[0] )