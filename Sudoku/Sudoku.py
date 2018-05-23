import random
import copy
from Tile import Tile
import time
import math
# david supports you -\_(``/)_/-

class Board:

	def __init__(self):
		return

	def create(self):
		self.board = [[Tile(x,y,None) for x in range(9)]for y in range(9)]
		fillSuccess = False
		attempts = 0
		while not(fillSuccess):
			fillSuccess = self.fill()
			attempts+=1
			print("attempt " + str(attempts))

		#self.board = self.removeRandom(solvedBoard)

	def fill(self):
		fillSuccess = True
		for x in range(9):
			for y in range(9):
				if not (self.randomControlled(self.board[x][y])):
					fillSuccess = False
		if fillSuccess:
			print("Board successfull")
		else:
			print("Board unsuccessful")
		self.display()
		return fillSuccess

	def randomControlled(self, tile):
		numList = [1,2,3,4,5,6,7,8,9]
		
		random.Random().shuffle(numList)
		random.seed()
		random.jumpahead(10)

		for i in numList:
			testTile = Tile(tile.x,tile.y,i)
			if self.fullTest(testTile):
				self.board[tile.x][tile.y].value = testTile.value
				return True
		return False

	def fullTest(self, tile):
		
		x = tile.x
		y = tile.y
		value = tile.value

		for xTest in range(9):
			if self.board[xTest][y].value == value:
				return False

		for yTest in range(9):
			if self.board[x][yTest].value == value:
				return False

		if x>3:
			blockX = 0
		elif x>6:
			blockX = 3
		else:
			blockX = 6
		if y>3:
			blockY = 0
		elif y>6:
			blockY = 3
		else:
			blockY = 6
		print(x, y, blockX, blockY)
		for blockXTest in range(blockX, blockX + 2, 1):
			for blockYTest in range(blockY, blockY + 2, 1):
				if self.board[blockXTest][blockYTest].value == value:
					return False
		
		return True

	def display(self):
		row = "{0}| {1}{2}{3} | {4}{5}{6} | {7}{8}{9}"
		border="------------------"
		print("\n\n$~$~$~$~$~$~$~$~$~$~$\n\n   123   456   789")
		eTotal = 0
		for yPrint in range(9):
			if yPrint % 3 == 0:
				print(border)
			valueList = [None]
			
			for i in range(9):
				if self.board[i][yPrint].value == None:
					valueList.append("x")
					eTotal += 1
				else:
					valueList.append(str(self.board[i][yPrint].value))
			valueList.remove(None)
			print(row.format(yPrint + 1, valueList[0],valueList[1],valueList[2],valueList[3],valueList[4],valueList[5],valueList[6],valueList[7],valueList[8]))
		print("\nUnplaceable tiles: " + str(eTotal))