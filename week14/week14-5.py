a=list(map(int, input().split() ))

ans=0

N= len(a)
for i in range(N-2):
	if a[i] ==a[-1]:
		ans += 1

print(ans)
		
		
a=list(map(int, input().split() ))

N=len(a)
for i in range(1,N):
	print(a[i]*a[i] , end=',');

print()