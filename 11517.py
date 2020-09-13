Infor= 105
Max_n = 10005

def atribui(k,total):
	memoria = [Infor] * Max_n
	memoria[0]=0
	for i in range(k):
		u=int(input())
		for i in range(u, Max_n):
			memoria[i] = min(memoria[i], memoria[i - u] + 1)
	while total < Max_n and memoria[total] == Infor:
			total += 1
	return '%d %d' % ((total, memoria[total]))
	
def main(args):
	n= int(input())
	if n <=10000:
		for i in range(n):
			total= int(input())
			quant=int(input())
			if quant <=100:
				print(atribui(quant,total))
	return 0
	
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

