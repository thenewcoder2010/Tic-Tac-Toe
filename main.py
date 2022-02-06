import turtle
def symbolDrawer(pen, symbol, position): # This function will draw the symbols in the position
	pen.penup()
	if symbol == "o": # All of the things will be executed if the symbol is o
		pen.color('white')
		pen.pensize(1)
		if position == 1: # Drawing the shape o for position 1
			pen.goto(-90,50)
			style = ("Arial", 30, "bold") # Setting up the font
			pen.write("O", font = style) # Writing O
		elif position == 2: # Drawing the shape o for position 2
			pen.goto(-40,50)
			style = ("Arial", 30, "bold")
			pen.write("O", font = style) # Writing O
		elif position == 3: # Drawing the shape o for position 3
			pen.goto(10,50)
			style = ("Arial", 30, "bold")
			pen.write("O", font = style)
		elif position == 4: # Drawing the shape o for position 4
			pen.goto(-90,0)
			style = ("Arial", 30, "bold")
			pen.write("O", font = style) # Writing O

		elif position == 5: # Drawing the shape o for position 5
			pen.goto(-40,0)
			style = ("Arial", 30, "bold")
			pen.write("O", font = style) # Writing O

		elif position == 6: # Drawing the shape o for position 6
			pen.goto(10,0)
			style = ("Arial", 30, "bold")
			pen.write("O", font = style) # Writing O

		elif position == 7: # Drawing the shape o for position 7
			pen.goto(-90,-50)
			style = ("Arial", 30, "bold")
			pen.write("O", font = style) # Writing O

		elif position == 8: # Drawing the shape o for position 8
			pen.goto(-40,-50)
			style = ("Arial", 30, "bold")
			pen.write("O", font = style) # Writing O

		elif position == 9: # Drawing the shape o for position 9
			pen.goto(10,-50)
			style = ("Arial", 30, "bold")
			pen.write("O", font = style) # Writing O
	elif symbol == "x": # All of the things in this block will be executed if the symbol is x
		pen.color('blue') # Setting the pen colour to Blue to make the game more aesthetic
		pen.pensize(2) # Making the pen more thick so it is more visible to the user
		if position == 1: # Drawing the shape x for position 1
			pen.goto(-90,50)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O
		elif position == 2: # Drawing the shape x for position 2
			pen.goto(-40,50)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O
		elif position == 3: # Drawing the shape x for position 3
			pen.goto(10,50)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O
		elif position == 4: # Drawing the shape x for position 4
			pen.goto(-90,0)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O
		elif position == 5: # Drawing the shape x for position 5
			pen.goto(-40,0)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O
		elif position == 6: # Drawing the shape x for position 6
			pen.goto(10,0)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O
		elif position == 7: # Drawing the shape x for position 7
			pen.goto(-90,-50)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O
		elif position == 8: # Drawing the shape x for position 8
			pen.goto(-40,-50)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O
		elif position == 9: # Drawing the shape x for position 9
			pen.goto(10,-50)
			style = ("Arial", 30, "bold")
			pen.write("X", font = style) # Writing O

def positionChecker(locations, position, symbol): # This function will be used to check if the position is taken
	if position == 1:
		if locations[0][0] == '': # Checking if the position is taken
			locations[0][0] = symbol # Setting the position to the input symbol
			return True
	elif position == 2:
		if locations[0][1] == '': # Checking if the position is taken
			locations[0][1] = symbol # Setting the position to the input symbol
			return True
	elif position == 3:
		if locations[0][2] == '': # Checking if the position is taken
			locations[0][2] = symbol # Setting the position to the input symbol
			return True
	elif position == 4:
		if locations[1][0] == '': # Checking if the position is taken
			locations[1][0] = symbol # Setting the position to the input symbol
			return True
	elif position == 5:
		if locations[1][1] == '': # Checking if the position is taken
			locations[1][1] = symbol # Setting the position to the input symbol
			return True
	elif position == 6:
		if locations[1][2] == '': # Checking if the position is taken
			locations[1][2] = symbol # Setting the position to the input symbol
			return True
	elif position == 7:
		if locations[2][0] == '': # Checking if the position is taken
			locations[2][0] = symbol # Setting the position to the input symbol
			return True
	elif position == 8:
		if locations[2][1] == '': # Checking if the position is taken
			locations[2][1] = symbol # Setting the position to the input symbol
			return True
	elif position == 9:
		if locations[2][2] == '': # Checking if the position is taken
			locations[2][2] = symbol # Setting the position to the input symbol
			return True

def winChecker(boardPositions, numberOfMoves):
	def result(player,):
		if player == "x":
			print("PLAYER 1 WINS!!!")
		elif player == "o":
			print("PLAYER 2 WINS!!!")
	if boardPositions[0][0] == boardPositions[0][1] == boardPositions[0][2]:
		winner = boardPositions[0][0]
		result(winner)
	elif boardPositions[1][0] == boardPositions[1][1] == boardPositions[1][2]:
		winner = boardPositions[1][0]
		result(winner)
	elif boardPositions[2][0] == boardPositions[2][1] == boardPositions[2][2]:
		winner = boardPositions[2][0]
		result(winner)
	elif boardPositions[0][0] == boardPositions[1][0] == boardPositions[2][0]:
		winner = boardPositions[0][0]
		result(winner)
	elif boardPositions[0][1] == boardPositions[1][1] == boardPositions[2][2]:
		winner = boardPositions[0][0]
		result(winner)
	elif boardPositions[0][2] == boardPositions[1][2] == boardPositions[2][2]:
		winner = boardPositions[0][0]
		result(winner)
	elif numberOfMoves == 9:
		print("IT'S A TIE")

myPen = turtle.Turtle() # Setting up the pen
myPen.speed(0) # Setting the speed to 0 so I can test my code quickly
myPen.penup()
myPen.goto(50,-50) # Going to the bottom right corner of the square

myPen.color('red', 'red') # Changing the outline to red and the internal colour to red
myPen.pendown()
myPen.right(180)
myPen.begin_fill()
for i in range(4): # Creating the square
	myPen.forward(150)
	myPen.right(90)
myPen.end_fill() # Filling the sqaure with the red colour

myPen.penup()
myPen.forward(100) # Going to the location of where the first line is going to be drawn
myPen.right(90) # Moving the pen 90˚

myPen.color('white') # Changing the pen color to white
myPen.pendown()
myPen.forward(150) # Drawing the first vertical line

myPen.penup()
myPen.right(90)
myPen.forward(50)
myPen.right(90)

myPen.pendown()
myPen.forward(150) # Drawing the second vertical line

myPen.penup()
myPen.left(90)
myPen.penup()
myPen.forward(50)

myPen.left(90)
myPen.forward(50)

myPen.left(90)
myPen.pendown()
myPen.forward(150) # Drawing the first horizontal line

myPen.right(90)
myPen.penup()
myPen.forward(50)

myPen.right(90)
myPen.pendown()
myPen.forward(150) # Drawing the second horizontal line

myPen.penup()
myPen.color('black')
myPen.goto(-100, -75)
labelingsytle = ("Arial", 10, "bold")
myPen.write("Player 1: X Player 2: O", font = labelingsytle)
board = [
	['', '', ''],
	['', '', ''],
	['', '', ''],
]
counter = 0
while not counter == 9:
	if counter % 2 == 0 and counter != 9: # Checking if it is player 1's turn or player 2's turn
		inputPosition = int(input("Player-1 (1-9): "))
		inputSymbol = "x"
		if inputPosition > 0 and inputPosition < 10: # Checking if the position is valid
			result = positionChecker(board, inputPosition, inputSymbol)
			if result == True:
				symbolDrawer(myPen, inputSymbol, inputPosition) # Calling the function
				counter += 1
	if counter % 2 == 1 and counter != 9: # Checking if it is player 1's turn or player 2's turn
		inputPosition = int(input("Player-2 (1-9): "))
		inputSymbol = "o"
		if inputPosition > 0 and inputPosition < 10: # Checking if the position is valid
			result = positionChecker(board, inputPosition, inputSymbol)
			if result == True:
				symbolDrawer(myPen, inputSymbol, inputPosition) # Calling the function
				counter += 1