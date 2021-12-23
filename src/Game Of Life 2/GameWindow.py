import SaveAndLoad
import tkinter

class GameWindow:
#
# Begin definitions
#
    # No functionality in current iteration
    def __init__(self):
        print("Creating gameWindow object")

    # To print 2d arrays in a more readable format
    def betterPrint(self,arr):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

        for i in range(len(arr)):
            print(arr[i])
            print("\n")

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # To create the window and fill it with buttons
    def createWindow(self,size):
        self.gridSize = size
        
        self.statusArray = [[]]*self.gridSize
        for i in range(self.gridSize):
            self.statusArray[i] = [0]*self.gridSize

        self.toBeChangedArray = [[]]*self.gridSize
        for i in range(self.gridSize):
            self.toBeChangedArray[i] = [0]*self.gridSize

        self.frameArray = [[]]*self.gridSize
        for i in range(self.gridSize):
            self.frameArray[i] = [0]*self.gridSize

        self.buttonArray = [[]]*self.gridSize
        for i in range(self.gridSize):
            self.buttonArray[i] = [0]*self.gridSize

        self.saveHandler = SaveAndLoad.SaveAndLoad()

        self.window = tkinter.Tk()
        self.window.bind("<t>",self.updateFunction)
        self.window.bind("<l>",self.saveHandler.prepareWindow)

        self.starDog = tkinter.PhotoImage(file="StarryDoge.png")
        self.curseDog = tkinter.PhotoImage(file="CursedDoge.png")

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.frameArray[i][j] = tkinter.Frame(master=self.window)
                self.frameArray[i][j].grid(row=i,column=j,padx=0,pady=0)

                self.buttonArray[i][j] = tkinter.Button(master=self.frameArray[i][j],image=self.starDog)

                self.buttonArray[i][j].bind("<Button-1>",self.flipClickedCell)

                self.buttonArray[i][j].pack()
        self.window.mainloop()

    # Toggle the cell at the given coordinates
    def flipCell(self,x,y):
        if self.statusArray[x][y] == 0:

            self.statusArray[x][y] = 1
            self.buttonArray[x][y].configure(image=self.curseDog)

        elif self.statusArray[x][y] == 1:

            self.statusArray[x][y] = 0
            self.buttonArray[x][y].configure(image=self.starDog)

        else:
            print("something went very wrong with cell switching")

    # Call flipCell() when button is clicked
    def flipClickedCell(self,event):
        info = event.widget.master.grid_info()

        self.flipCell(info["row"],info["column"])

        self.betterPrint(self.statusArray)

    # Sum up the number of active neighbors of the given cell
    def calculateNeighbors(self,i,j):
        if i == 0:
        # if it's the top row
            if j == 0:
            #if it's the leftmost column
                return self.statusArray[i][j+1] + self.statusArray[i+1][j] + self.statusArray[i+1][j+1]
            elif j == len(self.statusArray[i]) - 1:
            #if it's the rightmost column
                return self.statusArray[i][j-1] + self.statusArray[i+1][j-1] + self.statusArray[i+1][j]
            else:
            #it's a top row middle cell
                return self.statusArray[i][j-1] + self.statusArray[i][j+1] + self.statusArray[i+1][j-1] + self.statusArray[i+1][j] + self.statusArray[i+1][j+1]

        elif i == len(self.statusArray) - 1:
        #if it's the bottom row
            if j == 0:
            #if it's the leftmost column
                return self.statusArray[i-1][j] + self.statusArray[i-1][j+1] + self.statusArray[i][j+1]
            elif j == len(self.statusArray[i]) - 1:
            #if it's the rightmost column
                return self.statusArray[i-1][j-1] + self.statusArray[i-1][j] + self.statusArray[i][j-1]
            else:
            #it's a bottom row middle cell
                return self.statusArray[i-1][j-1] + self.statusArray[i-1][j] + self.statusArray[i-1][j+1] + self.statusArray[i][j-1] + self.statusArray[i][j+1]

        elif j == 0:
        # if it's the leftmost column and a middle row
            return self.statusArray[i-1][j] + self.statusArray[i-1][j+1] + self.statusArray[i][j+1] + self.statusArray[i+1][j] + self.statusArray[i+1][j+1]

        elif j == len(self.statusArray[i]) - 1:
        # if it's the rightmost column and a middle row
            return self.statusArray[i-1][j-1] + self.statusArray[i-1][j] + self.statusArray[i][j-1] + self.statusArray[i+1][j-1] + self.statusArray[i+1][j]

        else:
        # it's a middle cell
            return self.statusArray[i-1][j-1] + self.statusArray[i-1][j] + self.statusArray[i-1][j+1] + self.statusArray[i][j-1] + self.statusArray[i][j+1] + self.statusArray[i+1][j-1] + self.statusArray[i+1][j] + self.statusArray[i+1][j+1]

    #   for each row:
    #       for each column:
    #          determine if cell needs to die/live, store value to toBeChangedArray[i][j]
    #   
    #   for each row:
    #       for each column:
    #           if stateArray[i][j] != toBeChangedArray[i][j]
    #               flip buttonArray[i][j]
    def updateFunction(self,event):
    
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                neighborCount = self.calculateNeighbors(i,j)
                if neighborCount < 2:
                    self.toBeChangedArray[i][j] = 0
                elif neighborCount == 2:
                    self.toBeChangedArray[i][j] = self.statusArray[i][j]
                elif neighborCount == 3:
                    self.toBeChangedArray[i][j] = 1
                elif neighborCount > 3:
                    self.toBeChangedArray[i][j] = 0

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if self.statusArray[i][j] != self.toBeChangedArray[i][j]:
                    self.flipCell(i,j)