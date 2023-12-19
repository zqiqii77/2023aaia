a,b=list(map(int, input().split() ))

ans=a//b
if a%b>0: ans += 1

print(ans, end='')

a=list(map(int,input().split() ))
for i in range(10-1,-1, -1):
	print(a[i], end=' ')
	
	
	a=list(map(int,input().split() ))
if a>0 and b>0: ans = 1
if a<0 and b>0: ans = 2
if a<0 and b<0: ans = 3
if a>0 and b<0: ans = 4
print(ans)


a=list(map(int,input().split() ))
if a>0 and b>0: ans = 1
if a<0 and b>0: ans = 2
if a<0 and b<0: ans = 3
if a>0 and b<0: ans = 4
print(ans),b,c,d=list(map(int, input().split() ))

ans = (a-c) * (b-d)
if ans<0: ans = -ans
print(ans, end='')