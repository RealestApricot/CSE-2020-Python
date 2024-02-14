import math

def ReadSquare() -> list[list[int]]:
	SquareToReturn = []
	FileToRead = open("Lab1/square11A.txt", "r")
	NumbersRead = []
	for line in FileToRead:
		for Number in line.split():
			NumbersRead.append(int(Number))
	SquareLength = int(len(NumbersRead) ** (1/2))
	NumberIndex = 0
	for Index in range(SquareLength):
		NewRow = []
		for Jindex in range(SquareLength):
			NewRow.append(NumbersRead[NumberIndex])
			NumberIndex += 1
		SquareToReturn.append(NewRow)
	
	FileToRead.close()
	return SquareToReturn

def PrintSquare(Square) -> None:
	for Row in Square:
		for Number in Row:
			if Number == 0:
				print("{:<}".format("~"), end = "	")
			else:
				print("{:<}".format(str(Number)), end = "	")
		
		print("\n")

def RowSum(Square, Row) -> int:
	Sum = 0
	for Number in Square[Row]:
		Sum += Number
	return Sum

def ColSum(Square, Col) -> int:
	Sum = 0
	for Row in Square:
		Sum += Row[Col]
	return Sum

def FirstDiagonalSum(Square) -> int:
	Sum = 0
	for Index in range(len(Square)):
		Sum += Square[Index][Index]
	return Sum

def SecondDiagonalSum(Square) -> int:
	Sum = 0
	for Index in range(len(Square)):
		Sum += Square[Index][len(Square) - Index - 1]
	return Sum

def CheckSquare(Square) -> tuple[bool, int]:
	print("Checking for magic square", end = "\n")
	
	SquareLength = len(Square)
	FirstRowSum = RowSum(Square, 0)
	
	for Index in range(SquareLength):
		if RowSum(Square, Index) != FirstRowSum or ColSum(Square, Index) != FirstRowSum:
			return False, None
		if FirstDiagonalSum(Square) != FirstRowSum or SecondDiagonalSum(Square) != FirstRowSum:
			return False, None
	
	return True, FirstRowSum

def main() -> None:
	Square = ReadSquare()
	PrintSquare(Square)
	IsMagicSquare, MagicNumber = CheckSquare(Square)
	if IsMagicSquare:
		print("This is a magic square with magic number", MagicNumber)
	else:
		print("This is not a magic square")

main()