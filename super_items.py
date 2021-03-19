from outline import gameOutline
import colorama
from colorama import *
# from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)


class Item():
    def __init__(self, x, y, path, forecolour, backcolour):
        self.x = x
        self.y = y
        #if (path != "power_expand.txt"):
        self.generate(path, forecolour, backcolour)

    def generate(self, path, forecolour, backcolour):
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
                                                   j] = forecolour + backcolour + self.arr[i][j]

    def clearOnLiveLost(self, itemobj):
        for i in range(0, itemobj.height):
            for j in range(0, len(itemobj.arr[i])):
                gameOutline.OutlineArray[itemobj.y + i][itemobj.x +
                                                        j] = Fore.BLACK + Back.BLACK + " "
        #self.lifelost = 1
