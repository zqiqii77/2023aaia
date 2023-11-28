a = int(input())

ans=0
for i in range(1,a+1):
	ans += i*i

print(ans, end='')

a,b=list(map(int, input().split() ))

ans=0
for i in range(a,b+1):
	if i%3==0: ans +=i
print(ans, end='')


N=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
for i in range(N):
	print(a[i]+b[i],end=' ')
    
    
    a=list(map(int, input().split()))

ans=0
for i in a:
	if i>0: ans += i
	
print(ans, end='')