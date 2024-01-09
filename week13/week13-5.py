上午2:27
你傳送了
a=list(map(int,input().split()))
N=len(a)-1
for i in range(N-1,-1,-1):
	print(a[i],end=' ')
print()




a=int(input())
ans=0
for i in range(1,a):
	ans+=i*(i+1)
print(ans)