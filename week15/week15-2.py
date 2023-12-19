a=list(map(int,input().split() ))

print(max(a) - min(a),end='' )


ans=0

while True:
	a=input('Enter an integer ( 999 to end ): \n')
	a=int(a)
	if a ==999:
		break
	ans+=a
	
print('The total is:',	ans	,	end='')