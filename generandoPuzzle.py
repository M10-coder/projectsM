import random
import numpy as np
# numbers to display in grid
elibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# base list to create 9*9 array
listModel = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# object that will be my gameBoard
class grid:
    # matriz that holds the values
    matrix = []
    matrixFinal = []
    # sets that form 9 blocks
    setA1 = []
    setA2 = []
    setA3 = []
    setB1 = []
    setB2 = []
    setB3 = []
    setC1 = []
    setC2 = []
    setC3 = []
    # filling the 9*9 grid
    def __init__(self, array, sample):
        self.array = array
        self.sample = sample
        for i in range(9):
            self.matrix.append(array)
        self.matrix = np.array(self.matrix)
    # getting the 3 elements for each row
    def generatingSetA(self):
        self.setA1 = random.sample(self.sample, 3)
        self.setA2 = random.sample(self.sample, 3)
        self.setA3 = random.sample(self.sample, 3)
        # making sure values are eligble for each row
        counter = 0
        for i in self.setA2:
            if i in self.setA1:
                counter += 1
        loop = 0
        while counter > 0:
            for i in self.setA2:

                loop += 1
                if i in self.setA1:
                    counter += 1
                    self.setA2 = (random.sample(self.sample, 3))
                    loop = 0
                else:
                    if loop > len(self.setA1) - 1:
                        counter = 0
        # putting both sets together and testing if they are eligible
        setsTotal = []
        for i in self.setA1:
            i = int(i)
            setsTotal.append(i)
        for i in self.setA2:
            i = int(i)
            setsTotal.append(i)
        counter = 1
        while counter > 0:
            for i in self.setA3:
                loop += 1
                if i in setsTotal:
                    counter += 1
                    self.setA3 = list(random.sample(self.sample, 3))
                    loop = 0
                else:
                    if loop > len(setsTotal) - 1:
                        counter = 0
    # swapping elements positions from setsA
    def swapingPositions(self):
        # assigning initial values to setB
        self.setB1 = self.setA1
        self.setB2 = self.setA3
        self.setB3 = self.setA2
        # swaping postions for set B1
        aux = self.setB1[0]
        self.setB1[0] = self.setB1[1]
        self.setB1[1] = self.setB1[2]
        self.setB1[2] = aux
        # swaping postions for set B2
        aux = self.setB2[0]
        self.setB2[0] = self.setB2[1]
        self.setB2[1] = self.setB2[2]
        self.setB2[2] = aux
        # swaping postions for set B3
        aux = self.setB3[0]
        self.setB3[0] = self.setB3[1]
        self.setB3[1] = self.setB3[2]
        self.setB3[2] = aux
        # swapping for setC
        self.setC1 = self.setA1
        self.setC2 = self.setA3
        self.setC3 = self.setA2
        # swappin for setC1
        aux = self.setC1[0]
        self.setC1[0] = self.setC1[1]
        self.setC1[1] = self.setC1[2]
        self.setC1[2] = aux
        # swappin for setC2
        aux = self.setC2[0]
        self.setC2[0] = self.setC2[1]
        self.setC2[1] = self.setC2[2]
        self.setC2[2] = aux
        # swappin for setC3
        aux = self.setC3[0]
        self.setC3[0] = self.setC3[1]
        self.setC3[1] = self.setC3[2]
        self.setC3[2] = aux
        # Adding every value from sets A to main matrix
    def addingSetsA(self):
        counter = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                    #
                while counter < 3:
                    for x in range(len(self.setA1)):
                        self.matrix[0][0 + counter] = self.setA1[x]
                        self.matrix[1][3 + counter] = self.setA1[x]
                        self.matrix[2][6 + counter] = self.setA1[x]
                        counter += 1
                    counter = 0
                    for x in range(len(self.setA1)):
                        self.matrix[0][3 + counter] = self.setA2[x]
                        self.matrix[1][6 + counter] = self.setA2[x]
                        # self.matrix[2][6 + counter] = self.setA1[x]
                        counter += 1
                    counter = 0
                    for x in range(len(self.setA1)):
                        self.matrix[0][6 + counter] = self.setA3[x]
                        self.matrix[1][0 + counter] = self.setA3[x]
                        counter += 1
                    counter = 0
                    for x in range(len(self.setA1)):
                        self.matrix[2][0 + counter] = self.setA2[x]
                        self.matrix[2][3 + counter] = self.setA3[x]
                        counter += 1
    #adding values of sets B
    def addingSetB(self):
        counter = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                while counter < 3:
                    for x in range(len(self.setB1)):
                        self.matrix[3][0 + counter] = self.setB1[x]
                        self.matrix[4][0 + counter] = self.setB2[x]
                        self.matrix[5][0 + counter] = self.setB3[x]
                        counter += 1
                    counter = 0
                    for x in range(len(self.setB1)):
                        self.matrix[3][3 + counter] = self.setB3[x]
                        self.matrix[4][3 + counter] = self.setB1[x]
                        self.matrix[5][3 + counter] = self.setB2[x]
                        counter += 1
                    counter = 0
                    for x in range(len(self.setB1)):
                        self.matrix[3][6 + counter] = self.setB2[x]
                        self.matrix[4][6 + counter] = self.setB3[x]
                        self.matrix[5][6 + counter] = self.setB1[x]
                        counter += 1
    # adding values of sets C
    def addingSetC(self):
        counter = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                while counter < 3:
                    for x in range(len(self.setC3)):
                        self.matrix[6][0 + counter] = self.setC1[x]
                        self.matrix[7][0 + counter] = self.setC3[x]
                        self.matrix[8][0 + counter] = self.setC2[x]
                        counter += 1
                    counter = 0
                    for x in range(len(self.setC3)):
                        self.matrix[6][3 + counter] = self.setC2[x]
                        self.matrix[7][3 + counter] = self.setC1[x]
                        self.matrix[8][3 + counter] = self.setC3[x]
                        counter += 1
                    counter = 0
                    for x in range(len(self.setC3)):
                        self.matrix[6][6 + counter] = self.setC3[x]
                        self.matrix[7][6 + counter] = self.setC2[x]
                        self.matrix[8][6 + counter] = self.setC1[x]
                        counter += 1
    # swapping rows
    def swappingRows(self):
        row0 = []
        row1 = []
        row2 = []
        row3= []
        row4 = []
        row5 = []
        row6 = []
        row7 = []
        row8 = []
        def rows(r, p):
            counter = 0
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    while counter < 9:
                        r.append(self.matrix[p][0 + counter])
                        counter += 1
        rows(row0,0)
        rows(row1, 1)
        rows(row2, 2)
        rows(row3, 3)
        rows(row4, 4)
        rows(row5, 5)
        rows(row6, 6)
        rows(row7, 7)
        rows(row8, 8)
        def mixingRows(r,p):
            counter = 0
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    while counter < 9:
                        for x in range(9):
                            self.matrix[p][0 + counter] = r[x]
                            counter += 1
        mixingRows(row3,0)
        mixingRows(row2, 1)
        mixingRows(row1, 2)

        mixingRows(row0, 3)
        mixingRows(row5, 4)
        mixingRows(row4, 5)

        mixingRows(row6, 7)
        mixingRows(row7, 6)
    # function the shows final matrix

    def showGrid(self):
        for lines in self.matrix:
            print(lines)
a = grid(listModel, elibleNumbers)
a.generatingSetA()
a.addingSetsA()
a.swapingPositions()
a.addingSetB()
a.swapingPositions()
a.addingSetC()
a.swappingRows()


p = a.matrix