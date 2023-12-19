a=int(input())

ans=0
for i in range(1,1001):
	if a ==i*i:
		ans=i
		
print(ans, end='')

a=int(input())

import math
b=int(math.sqrt(a))

if a ==b*b:
	print(b, end='')
else:
	print(0, end='')