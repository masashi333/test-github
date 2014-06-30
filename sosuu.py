#coding:UTF-8
def prime1(n):
	#普通の素数表示プログラム
	for i in range(2,n+1):
		for j in range(2,i+1):
			if i%j ==0:
				break
		if i==j:
			print i,'',


prime1(100)
prime2(50)
prime3(300)
