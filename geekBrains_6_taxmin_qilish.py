#raqamni taxmin qiling
import random
son = int(input())
start = 1
end = 100
belgi = None
while belgi != "=":
	n = random.randint(start , end)
	print(n)
	belgi = input()
	if belgi == '>':
		start = n+1
	elif belgi == '<':
		end = n-1
	
print('pobeda', n)

