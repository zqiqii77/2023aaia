a= int(input())

ans=0
while a>0:
	ans=ans * 10 +a%10
	a=	a//10
print(ans)


a=input()

if a[0]==a[3] and a[1]==a[2]:
	print("YES")
else:
	print("NO")