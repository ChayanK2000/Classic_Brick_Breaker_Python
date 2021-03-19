import getch
import sys
# from getch import _getChUnix as getChar
from super_items import *
from outline import gameOutline
from collision import *
from bricks import *
from manage import *
import numpy as np
import colorama
from colorama import *
# from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

# inheritance (in classes) + polymorphism(in variables like height and functions like move, clearOnLiveLost etc)


class Paddle(Item):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        # self.lifelost = 0  # dummy variable just to check whether the life is just lost or not

        # making the partitions
        self.centrewidth = self.width % 4
        self.partitions()

    def partitions(self):
        self.partwidth = self.width // 4
        self.left2 = []
        self.left1 = []
        self.centre = []
        self.right1 = []
        self.right2 = []
        self.pos = self.x
        for i in range(0, 5): # as total five partitions
            if i == 2:
                max = self.centrewidth
            else:
                max = self.partwidth

            for j in range(0, max):
                if (i == 0):
                    self.left2.append(self.pos + j)
                if (i == 1):
                    self.left1.append(self.pos + j)
                if (i == 2):
                    self.centre.append(self.pos + j)
                if (i == 3):
                    self.right1.append(self.pos + j)
                if (i == 4):
                    self.right2.append(self.pos + j)
            self.pos += j + 1
        self.left2 = np.array(self.left2)
        self.left1 = np.array(self.left1)
        self.centre = np.array(self.centre)
        self.right1 = np.array(self.right1)
        self.right2 = np.array(self.right2)

    def changePartCoord(self, bit):
        self.left2 += bit
        self.left1 += bit
        self.centre += bit
        self.right1 += bit
        self.right2 += bit
        # print(self.left2)
        # print(self.left1)
        # print(self.centre)
        # print(self.right1)
        # print(self.right2)
        # exit()

    def move(self, char):

        if char == 'j':
            for i in range(0, self.height):
                for j in range(0, len(self.arr[i])):
                    gameOutline.OutlineArray[self.y + i][self.x +
                                                         j] = Fore.BLACK + Back.BLACK + " "

            if(self.x >= 1):
                self.x = self.x - 1
                self.changePartCoord(-1) # to move 1 unit left
                if (Ballobj.rest == True):
                    gameOutline.OutlineArray[Ballobj.y][Ballobj.x] = Fore.BLACK + \
                        Back.BLACK + " "
                    Ballobj.x -= 1
                    gameOutline.OutlineArray[Ballobj.y][Ballobj.x] = Fore.GREEN + \
                        Back.BLACK + "O"

            for i in range(0, self.height):
                for j in range(0, len(self.arr[i])):
                    gameOutline.OutlineArray[self.y + i][self.x +
                                                         j] = Fore.GREEN + Back.BLACK + self.arr[i][j]
            # gameOutline.display()
        elif char == 'l':
            for i in range(0, self.height):
                for j in range(0, len(self.arr[i])):
                    gameOutline.OutlineArray[self.y + i][self.x +
                                                         j] = Fore.BLACK + Back.BLACK + " "

            if(self.x + self.width <= 99):
                self.x = self.x + 1
                self.changePartCoord(1)  # to move 1 unit right
                if (Ballobj.rest == True):
                    gameOutline.OutlineArray[Ballobj.y][Ballobj.x] = Fore.BLACK + \
                        Back.BLACK + " "
                    Ballobj.x += 1
                    gameOutline.OutlineArray[Ballobj.y][Ballobj.x] = Fore.GREEN + \
                        Back.BLACK + "O"

            for i in range(0, self.height):
                for j in range(0, len(self.arr[i])):
                    gameOutline.OutlineArray[self.y + i][self.x +
                                                         j] = Fore.GREEN + Back.BLACK + self.arr[i][j]
            # gameOutline.display()


class Ball(Item):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        self.vel_x = 0
        self.vel_y = 0
        self.fire = 0
        #self.history = 0
        self.lifelost = 0  # dummy variable just to check whether the life is just lost or not
        self.rest = True # variable telling whther ball is at rest(on paddle) or moving

    def move(self, char):
        if char == ' ' and self.rest == True: #Bug: have to keep pressing space(or any char) to release the ball
            self.vel_y = -1
            self.rest = False

        #writing this collision para here as the values of x, y are changing andprinted here

        collision_paddle(Ballobj, Paddleobj)
        collision_brick(Ballobj, red_bricks_obj, "red")
        collision_brick(Ballobj, blue_bricks_obj, "blue")
        collision_brick(Ballobj, cyan_bricks_obj, "cyan")
        collision_brick(Ballobj, unbreak_bricks_obj, "unbreakable")
        collision_brick(Ballobj, expl_bricks_obj, "explosive")
        collision_brick(Ballobj, list(rainbow_bricks_obj.values()), "rainbow")
        collision_wall(Ballobj, Paddleobj)

        # this history variable just so that when ball passes a brick at high velocity, the gap is not created
        if self.lifelost == 0:
            #if (self.history == 0):
            gameOutline.OutlineArray[self.y][self.x] = Fore.BLACK + \
                Back.BLACK + " "

            #self.history = 0
            self.x += self.vel_x
            self.y += self.vel_y

            # if (gameOutline.OutlineArray[self.y][self.x] != Fore.BLACK + Back.BLACK + " "):
            #     self.history = 1

            #else:
            if self.fire == 1:
                gameOutline.OutlineArray[self.y][self.x] = Fore.RED + \
                    Back.BLACK + "O"
            else:
                gameOutline.OutlineArray[self.y][self.x] = Fore.GREEN + Back.BLACK + "O"
        else:  # re initializing and generating like at the start
            self.lifelost = 0
            Paddleobj.x = 40
            Paddleobj.y = 29
            self.x = 49
            self.y = 28
            self.vel_x, self.vel_y = 0, 0
            self.fire = 0
            self.rest = True
            Paddleobj.generate('paddle.txt', Fore.GREEN, Back.BLACK)
            self.generate('ball1.txt', Fore.GREEN, Back.BLACK)
            Paddleobj.partitions()
            # if (self.lives == 0):  # to end program. thinking to write this in main.py
            #     exit()


Ballobj = Ball(49, 28, 'ball1.txt', Fore.GREEN, Back.BLACK)

Paddleobj = Paddle(40, 29, 'paddle.txt', Fore.GREEN, Back.BLACK)
