import random
from tkinter import *

playerCharPosX = random.randint(-5,5)
playerCharPosY = random.randint(-5,5)
wumpusCharPosX = random.randint(-5,5)
wumpusCharPosY = random.randint(-5,5)
playerCharShots = 3
isPlayerAlive = True
wumpusIsNearby = "You smell a wumpus."
batsAreNearby = "You hear bats."
pitIsNearby = "You feel a breeze."
isNearbyField = ""

while wumpusCharPosX == playerCharPosX and wwumpusCharPosY == playerCharPosY:
	wumpusCharPosX = random.randint(-5,5)
	wumpusCharPosY = random.randint(-5,5)


class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.pack(fill = BOTH, expand = 1)

		self.playerCoordinateLabel = Label(text = "", fg = "BLUE", font = ("Helvetica 10 bold"), height = 1, width = 3)
		self.playerCoordinateLabel.place(x = 30, y = 33)

		self.locationTagLabel = Label(text = "Position", fg = "ORANGE", font = ("Helvetica 10 bold"), relief = GROOVE)
		self.locationTagLabel.place(x = 15, y = 90)
		
		self.shootTagLabel = Label(text = "Shoot", fg = "ORANGE", font = ("Helvetica 10 bold"), relief = GROOVE)
		self.shootTagLabel.place(x = 105, y = 90)

		self.nearbyLabel = Label(text = "", fg = "GRAY", font = ("Helvetica 8"), height = 1, width = 64)
		self.nearbyLabel.place(x = 150, y = 65)

		self.moveLocationLabel = Label(text = "You moved north.", fg = "GRAY", font = ("Helvetica 8"), height = 1, width = 64)
		self.moveLocationLabel.place(x = 150, y = 0)

		self.update_player_position()

		moveNorthButton = Button(self, text="N", command=self.clickMoveNorthButton, height = 1, width = 1)
		moveNorthButton.place(x = 35, y = 0)

		moveSouthButton = Button(self, text="S", command=self.clickMoveSouthButton, height = 1, width = 1)
		moveSouthButton.place(x = 35, y = 60)

		moveEastButton = Button(self, text="E", command=self.clickMoveEastButton, height = 1, width = 1)
		moveEastButton.place(x = 60, y = 30)

		moveWestButton = Button(self, text="W", command=self.clickMoveWestButton, height = 1, width = 1)
		moveWestButton.place(x = 10, y = 30)

		lookNorthButton = Button(self, text="N", command=self.clickShootNorthButton, height = 1, width = 1)
		lookNorthButton.place(x = 115, y = 0)

		lookSouthButton = Button(self, text="S", command=self.clickShootSouthButton, height = 1, width = 1)
		lookSouthButton.place(x = 115, y = 60)

		lookEastButton = Button(self, text="E", command=self.clickShootEastButton, height = 1, width = 1)
		lookEastButton.place(x = 140, y = 30)

		lookWestButton = Button(self, text="W", command=self.clickShootWestButton, height = 1, width = 1)
		lookWestButton.place(x = 90, y = 30)

		menu = Menu(self.master)
		self.master.config(menu = menu)

		fileMenu = Menu(menu)
		fileMenu.add_command(label = "Exit", command = self.exitProgram)
		menu.add_cascade(label = "File", menu = fileMenu)

	def update_player_position(self):
		global playerCharPosX
		global playerCharPosY
		global wumpusCharPosX
		global wumpusCharPosY
		global isNearbyField
		self.playerCoordinateLabel.configure(text=str(playerCharPosX)+","+str(playerCharPosY))
		if (playerCharPosY + 1 == wumpusCharPosY and playerCharPosX == wumpusCharPosX) or (playerCharPosY - 1 == wumpusCharPosY and playerCharPosX == wumpusCharPosX) or (playerCharPosX + 1 == wumpusCharPosX and playerCharPosY == wumpusCharPosY) or (playerCharPosX - 1 == wumpusCharPosX and playerCharPosY == wumpusCharPosY) or (playerCharPosY + 1 == wumpusCharPosY and playerCharPosX + 1 == wumpusCharPosX) or (playerCharPosY + 1 == wumpusCharPosY and playerCharPosX - 1 == wumpusCharPosX) or (playerCharPosY - 1 == wumpusCharPosY and playerCharPosX + 1 == wumpusCharPosX) or (playerCharPosY - 1 == wumpusCharPosY and playerCharPosX - 1 == wumpusCharPosX):
			isNearbyField = wumpusIsNearby
			self.nearbyLabel.configure(text=str(isNearbyField))
		elif playerCharPosX == wumpusCharPosX and playerCharPosY == wumpusCharPosY:
			self.nearbyLabel.configure(text=str("You were eaten by the wumpus!"))
			#add a death modifier here, find a way to make it function properly

	def clickMoveNorthButton(self):
		global playerCharPosY
		if playerCharPosY < 5:
			playerCharPosY = playerCharPosY + 1
			self.moveLocationLabel.configure(text="You moved north.")
		
		else:
			pass

		self.update_player_position()

	def clickMoveSouthButton(self):
		global playerCharPosY
		if playerCharPosY > -5:
			playerCharPosY = playerCharPosY - 1
			self.moveLocationLabel.configure(text="You moved south.")

		else:
			pass

		self.update_player_position()

	def clickMoveEastButton(self):
		global playerCharPosX
		if playerCharPosX < 5:
			playerCharPosX = playerCharPosX + 1
			self.moveLocationLabel.configure(text="You moved east.")

		else:
			pass

		self.update_player_position()

	def clickMoveWestButton(self):
		global playerCharPosX
		if playerCharPosX > -5:
			playerCharPosX = playerCharPosX - 1
			self.moveLocationLabel.configure(text="You moved west.")

		else:
			pass

		self.update_player_position()

	def clickShootNorthButton(self):
		pass

	def clickShootSouthButton(self):
		pass

	def clickShootEastButton(self):
		pass

	def clickShootWestButton(self):
		pass
		
	def exitProgram(self):
		exit()


# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("TK Hunt")
root.geometry("640x120")

# show window
root.mainloop()