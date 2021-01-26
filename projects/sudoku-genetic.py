#!/usr/bin/python3

from math import *
import os
import sys 
import random


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


def pc(text, ll) :
	print(text)
	form = "%3d "
	form = 3*form+"   "
	form = 3*form+"\n"
	form = 3*form+"\n"
	form = 3*form+"\n"
	print(form % tuple(ll) )
#    test where function
#clist = []
#rlist = []
#slist = []
#for idx in range(81) :
#	idxrow, idxcol, idxsqr = where(idx)
#	rlist.append(idxrow)
#	clist.append(idxcol)
#	slist.append(idxsqr)
#pc("rows", rlist)
#pc("cols", clist)
#pc("sqrs", slist)










class versuch :
	def __init__(self, board) :
		self.tt = list(board)
		self.conflict = 1000
		self.conf = 81*[1000]

	def fill(self) :
		for i,f in enumerate(self.tt) :
			if f == 0 :  self.tt[i] = int(random.random()*9+1)
		self.conflict = 1000
		self.conf = 81*[1000]
		self.test()


	def test(self) :
		tt = self.tt
		self.conflict = -9*9*3	
		self.conf = 81*[-3]    # each field conflicts with itself in the 3 tests 
		for idx in range(81) :
			idxrow, idxcol, idxsqr = where(idx)
			for j in row[idxrow] :
				if  tt[idx] == tt[j] : self.conf[idx] += 1
			for j in col[idxcol] :
				if  tt[idx] == tt[j] : self.conf[idx] += 1
			for j in sqr[idxsqr] :
				if  tt[idx] == tt[j] : self.conf[idx] += 1
		self.conflict = 0
		for idx in range(81) :
			self.conflict += self.conf[idx]
		return self.conflict

	def print(self) :
		#print "\033[94m" + l1 + "\033[0m"
		for i,f in enumerate(self.tt) :
			if board[i] :             formt = "\033[94m%d\033[0m "
			elif  self.conf[i] > 0 :  formt = "\033[91m%d\033[0m "
			else :                    formt = "\033[92m%d\033[0m "
			print(formt % (f), end="")
			if (i+1)%3 == 0 : print("  ", end='')
			if (i+1)%9 == 0 : print("")
			if (i+1)%27 == 0 : print("")
		print("conflict=", "\n\n")

	def mate(self, m) :
		p = versuch(board)
		for i,f in enumerate(m.tt) :
			if p.tt[i] == 0 :
				r =  random.random() 
				if r > 0.90 and not board[i] :
					p.tt[i] = int(random.random()*9+1)
				elif r > 0.46:
					p.tt[i]  = f
				else  :
					p.tt[i] = self.tt[i]
		return p

	def flip() :
		pass


#p = versuch(board)
#p.test()
#p.print()
#print('co',  p.conf)
#sys.exit()

npop = 5000
population = []
for i in range(npop) :
	p = versuch(board)
	p.fill()
	population.append(p)
population = sorted(population,  key=lambda x: x.conflict)
population[0].print()
population[-1].print()


cconf = 1000000
for iterations in range(30000) :
	for i in range(2000) :
		dad = population[int(random.random()*npop)]
		mom = population[int(random.random()*npop)]
		child=dad.mate(mom)
		child.test()
		population.append(child)

	population = sorted(population,  key=lambda x: x.conflict)
	if population[0].conflict < cconf :
		population[0].print()
		print("conflict=", [population[i].conflict for i in range(10)], "\n\n")
		cconf = population[0].conflict
	population = population[:npop] 	# kill the weaklings




