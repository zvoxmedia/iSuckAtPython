#!/usr/bin/python3

from math import *
import os
import sys 
import random


perfect = [	1,2,3, 4,5,6, 7,8,9,
		4,5,6, 7,8,9, 1,2,3,
		7,8,9, 1,2,3, 4,5,6,

		2,3,4, 5,6,7, 8,9,1,
		5,6,7, 8,9,1, 2,3,4,
		8,9,1, 2,3,4, 5,6,7,

		3,4,5, 6,7,8, 9,1,2,
		6,7,8, 9,1,2, 3,4,5,
		9,1,2, 3,4,5, 6,7,8,
	]

# P(n)=n!  n=9 P(9)=9!=362880
#362880*9*9= 29_393_280




board = [	9,0,6, 7,1,0, 0,0,2,
		0,2,0, 0,8,0, 0,9,0,
		0,0,1, 5,0,0, 8,0,3,

		0,0,0, 0,0,0, 2,0,6,
		6,3,0, 0,0,0, 0,1,7,
		2,0,4, 0,0,0, 0,0,0,

		4,0,2, 0,0,9, 1,0,0,
		0,1,0, 0,7,0, 0,3,0,
		3,0,0, 0,4,8, 9,0,5,
	]


board = [	1,0,0, 0,0,0, 4,0,0,
		0,2,0, 0,0,0, 0,0,0,
		0,0,3, 0,0,0, 0,0,0,

		0,0,0, 4,0,0, 0,0,0,
		0,0,0, 0,5,0, 0,0,0,
		0,0,0, 0,0,6, 0,0,0,

		0,0,0, 0,0,0, 7,0,0,
		0,0,0, 0,0,0, 0,8,0,
		0,0,0, 0,0,0, 0,0,9,
	]


row = (
		( 0, 1, 2,  3, 4, 5,  6, 7, 8),
		( 9,10,11, 12,13,14, 15,16,17),
		(18,19,20, 21,22,23, 24,25,26),

		(27,28,29, 30,31,32, 33,34,35),
		(36,37,38, 39,40,41, 42,43,44),
		(45,46,47, 48,49,50, 51,52,53),

		(54,55,56, 57,58,59, 60,61,62),
		(63,64,65, 66,67,68, 69,70,71),
		(72,73,74, 75,76,77, 78,79,80),
	)

col = (
		( 0, 9,18, 27,36,45, 54,63,72),
		( 1,10,19, 28,37,46, 55,64,73),
		( 2,11,20, 29,38,47, 56,65,74),

		( 3,12,21, 30,39,48, 57,66,75),
		( 4,13,22, 31,40,49, 58,67,76),
		( 5,14,23, 32,41,50, 59,68,77),

		( 6,15,24, 33,42,51, 60,69,78),
		( 7,16,25, 34,43,52, 61,70,79),
		( 8,17,26, 35,44,53, 62,71,80),
	)


sqr = (
		( 0, 1, 2,  9,10,11, 18,19,20),
		( 3, 4, 5, 12,13,14, 21,22,23),
		( 6, 7, 8, 15,16,17, 24,25,26),

		(27,28,29, 36,37,38, 45,46,47),
		(30,31,32, 39,40,41, 48,49,50),
		(33,34,35, 42,43,44, 51,52,53),

		(54,55,56, 63,64,65, 72,73,74),
		(57,58,59, 66,67,68, 75,76,77),
		(60,61,62, 69,70,71, 78,79,80),
	)

def where(idx):
	idxrow = int(idx/9)
	idxcol = idx % 9
	idxsqr = int(idxcol/3) + 3*int(idxrow/3)
	return (idxrow, idxcol, idxsqr)



def printboard(board, tboard) :
	for i,f in enumerate(tboard) :
		if board[i] :             formt = "\033[91m%d\033[0m "
		else :                    formt = "\033[92m%d\033[0m "
		print(formt % (f), end="")
		if (i+1)%3 == 0 : print("  ", end='')
		if (i+1)%9 == 0 : print("")
		if (i+1)%27 == 0 : print("")

def test(tt,idx, jj) :
	if tt[idx] : return 1000
	idxrow, idxcol, idxsqr = where(idx)
	conflict = 0
	for j in row[idxrow] :
		if  jj == tt[j] : conflict += 1
	for j in col[idxcol] :
		if  jj == tt[j] : conflict += 1
	for j in sqr[idxsqr] :
		if  jj == tt[j] : conflict += 1
	return conflict



def posibles(bb) :
	pp = []
	for idx in range(81) :
		ppp=[idx]
		for jj in range(1,10) :
			if  test(bb, idx, jj) == 0 : ppp.append( jj )

		if len(ppp) > 1: pp.append(ppp)
	pp = sorted(pp,  key=lambda x: len(x))
	print('pos',  pp)
	return pp




def solve(board, empty) :
	print("empty", empty)
	if not empty:
		print("solved")
		return board
	bb = list(board)	# make a copy to mess with

	pp = posibles(bb)
	if not pp :
		print('failed', empty)
		return []	# this means that there are empty places but none can be filled without conflict


	pbest = pp[0]
	ibest = pbest[0]
	for p in pbest[1:] :
		print('try ', p, ' in ', ibest, pbest)
		bb[ibest] = p
		result = solve(bb, empty-1)
		if result : return result
	print('failed*', empty)
	return []


empty = 81
for  b in board :
	if b :
		empty -= 1

result = solve(board, empty)
printboard(board, result)


