import getch
import sys
# from getch import _getChUnix as getChar
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


class Item():
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.generate(path)

    def generate(self, path):
        f = open(path, 'r')
        raw = f.read()
        raw = raw.rstrip("\n")
        self.arr = raw.splitlines()
        mx = -1
        for i in self.arr:
            mx = max(mx, len(i))

        self.height = len(self.arr)
        self.width = mx

        for i in range(self.height):

            for j in range(len(self.arr[i])):
                gameOutline.OutlineArray[self.y+i][self.x +
                                                   j] = Fore.GREEN + Back.BLACK + self.arr[i][j]

    def clearOnLiveLost(self, itemobj):
        for i in range(0, itemobj.height):
            for j in range(0, len(itemobj.arr[i])):
                gameOutline.OutlineArray[itemobj.y + i][itemobj.x +
                                                        j] = Fore.BLACK + Back.BLACK + " "
        self.lifelost = 1


class Paddle(Item):
    def __init__(self, x, y, path):
        super().__init__(x, y, path)
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
        for i in range(0, 5):
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
                self.changePartCoord(-1)
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
                self.changePartCoord(1)
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
    def __init__(self, x, y, path):
        super().__init__(x, y, path)
        self.vel_x = 0
        self.vel_y = 0
        self.lifelost = 0  # dummy variable just to check whether the life is just lost or not
        self.rest = True

    def move(self, char):
        if char == ' ' and self.rest == True:
            self.vel_y = -1
            self.rest = False

        collision_paddle(Ballobj, Paddleobj)
        collision_brick(Ballobj, red_bricks_obj, "red")
        collision_brick(Ballobj, blue_bricks_obj, "blue")
        collision_brick(Ballobj, cyan_bricks_obj, "cyan")
        collision_brick(Ballobj, unbreak_bricks_obj, "unbreakable")
        collision_brick(Ballobj, expl_bricks_obj, "explosive")
        collision_wall(Ballobj, Paddleobj)
        if self.lifelost == 0:
            gameOutline.OutlineArray[self.y][self.x] = Fore.BLACK + \
                Back.BLACK + " "

            self.x += self.vel_x
            self.y += self.vel_y

            gameOutline.OutlineArray[self.y][self.x] = Fore.GREEN + \
                Back.BLACK + "O"
        else:  # re initializing and generating like at the start
            self.lifelost = 0
            Paddleobj.x = 40
            Paddleobj.y = 29
            self.x = 49
            self.y = 28
            self.vel_x, self.vel_y = 0, 0
            self.rest = True
            Paddleobj.generate('paddle.txt')
            self.generate('ball1.txt')
            Paddleobj.partitions()
            # if (self.lives == 0):  # to end program. thinking to write this in main.py
            #     exit()


Ballobj = Ball(49, 28, 'ball1.txt')

Paddleobj = Paddle(40, 29, 'paddle.txt')
