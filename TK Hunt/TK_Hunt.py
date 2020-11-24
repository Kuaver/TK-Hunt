import math
import random
import time
from tkinter import *

playerInput = ""
playerCharPosX = 0
playerCharPosY = 0
monsterCharPosX = 0
monsterCharPosY = 0
playerCharShots = 0
isPlayerAlive = True
isGameRunning = True

class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.pack(fill = BOTH, expand = 1)

		self.playerLocationLabel = Label(text = "", fg = "BLUE", font = ("Helvetica 10 bold"), height = 1, width = 3)
		self.playerLocationLabel.place(x = 30, y = 33)
		self.update_player_position()

		self.locationLabel = Label(text = "Position", fg = "ORANGE", font = ("Helvetica 10 bold"), relief = GROOVE)
		self.locationLabel.place(x = 15, y = 90)
		
		self.locationLabel = Label(text = "Look", fg = "ORANGE", font = ("Helvetica 10 bold"), relief = GROOVE)
		self.locationLabel.place(x = 105, y = 90)

		moveNorthButton = Button(self, text="N", command=self.clickMoveNorthButton, height = 1, width = 1)
		moveNorthButton.place(x = 35, y = 0)

		moveSouthButton = Button(self, text="S", command=self.clickMoveSouthButton, height = 1, width = 1)
		moveSouthButton.place(x = 35, y = 60)

		moveEastButton = Button(self, text="E", command=self.clickMoveEastButton, height = 1, width = 1)
		moveEastButton.place(x = 60, y = 30)

		moveWestButton = Button(self, text="W", command=self.clickMoveWestButton, height = 1, width = 1)
		moveWestButton.place(x = 10, y = 30)

		lookNorthButton = Button(self, text="N", command=self.clickLookNorthButton, height = 1, width = 1)
		lookNorthButton.place(x = 115, y = 0)

		lookSouthButton = Button(self, text="S", command=self.clickLookSouthButton, height = 1, width = 1)
		lookSouthButton.place(x = 115, y = 60)

		lookEastButton = Button(self, text="E", command=self.clickLookEastButton, height = 1, width = 1)
		lookEastButton.place(x = 140, y = 30)

		lookWestButton = Button(self, text="W", command=self.clickLookWestButton, height = 1, width = 1)
		lookWestButton.place(x = 90, y = 30)

		menu = Menu(self.master)
		self.master.config(menu = menu)

		fileMenu = Menu(menu)
		fileMenu.add_command(label = "Exit", command = self.exitProgram)
		menu.add_cascade(label = "File", menu = fileMenu)

	def update_player_position(self):
		global playerCharPosX
		global playerCharPosY
		self.playerLocationLabel.configure(text=str(playerCharPosX)+","+str(playerCharPosY))

	def clickMoveNorthButton(self):
		global playerCharPosY
		if playerCharPosY < 5:
			playerCharPosY = playerCharPosY + 1
		
		else:
			pass

		self.update_player_position()

	def clickMoveSouthButton(self):
		global playerCharPosY
		if playerCharPosY > -5:
			playerCharPosY = playerCharPosY - 1

		else:
			pass

		self.update_player_position()

	def clickMoveEastButton(self):
		global playerCharPosX
		if playerCharPosX < 5:
			playerCharPosX = playerCharPosX + 1

		else:
			pass

		self.update_player_position()

	def clickMoveWestButton(self):
		global playerCharPosX
		if playerCharPosX > -5:
			playerCharPosX = playerCharPosX - 1

		else:
			pass

		self.update_player_position()

	def clickLookNorthButton(self):
		pass

	def clickLookSouthButton(self):
		pass

	def clickLookEastButton(self):
		pass

	def clickLookWestButton(self):
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