#!/usr/bin/python3


a = list(range(10,0,-1))
b=[]
c=[]


def move1( A, B) :
	x=A.pop()
	B.append(x)
	print( A, B)
	for i,x in enumerate(A, start=1) :
		if x > A[i-1] :
			print("%^%^%^")
print(a)
print(b)
print(c)


def moveN(n, A, B, C) :
	if n == 1 : 
		move1(A,B)
		return
	else:
		moveN(n-1, A,  C, B)
		move1(A,B)
		moveN(n-1, C,  B, A)


moveN(10, a,b,c)
print(a)
print(b)
print(c)

