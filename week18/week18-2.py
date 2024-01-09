a,b=list(map(int,input().split() ))
if a<b: ans=-1
if a==b: ans=0
if a>b: ans=1
print(ans)



a=int(input())
if a>=90:
	ans='A'
if 90 >a>=80:
	ans='B'
if 80 >a>=60:
	ans='c'
if a< 60:
	ans='F'
	
print(ans)


a=int(input())
if a%400==0:ans=1
elif a%100==0:ans=0
elif a%4==0:ans=1
else:ans=0

if ans==1:print(a, 'is a leap year.')
else:print(a, 'is not a leap year.')