a=input()

for c in a:
	if c!=' 'and c!='-':
		print(c)
		break
		
		
a=list(map(int, input().split() ))

a.sort()

for i in range(10-1, -1, -1):
	print(a[i], end=' ')
	
	
	
	
a=int(input())
b=int(input())

if a>b: ans = 1
if a==b: ans = 0
if a<b: ans = -1
print(ans,end='')