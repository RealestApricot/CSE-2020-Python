def Hello():
	print("Hello", end = "")

def World():
	print("World!", end = "")

def HelloWorld():
	Hello()
	print(", ", end = "")
	World()