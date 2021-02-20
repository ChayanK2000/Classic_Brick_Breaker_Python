from outline import gameOutline
import colorama
from colorama import *

# from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)


class Brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.strength = 1

    def clearbrick(self, Brick_obj, bricktype):
        for i in range(Brick_obj.height):

            for j in range(len(Brick_obj.arr[i])):
                gameOutline.OutlineArray[Brick_obj.y+i][Brick_obj.x +
                                                        j] = Fore.BLACK + Back.BLACK + " "

        if (bricktype == "red"):
            red_bricks_obj.remove(Brick_obj)
            objjj = Brick2_blue(Brick_obj.x, Brick_obj.y)
            blue_bricks_obj.append(objjj)
            objjj.generate("brick.txt")
        elif (bricktype == "blue"):
            blue_bricks_obj.remove(Brick_obj)
            objjj = Brick1_cyan(Brick_obj.x, Brick_obj.y)
            cyan_bricks_obj.append(objjj)
            objjj.generate("brick.txt")
        elif (bricktype == "cyan"):
            cyan_bricks_obj.remove(Brick_obj)


class Brick1_cyan(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)

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

        # char = np.array(([[Back.BLACK + Fore.BLACK + ' ' for col in range(width)]
        #                   for row in range(height)]))
        for i in range(self.height):

            for j in range(len(self.arr[i])):
                gameOutline.OutlineArray[self.y+i][self.x +
                                                   j] = Fore.CYAN + Back.CYAN + self.arr[i][j]


class Brick2_blue(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)

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

        # char = np.array(([[Back.BLACK + Fore.BLACK + ' ' for col in range(width)]
        #                   for row in range(height)]))
        for i in range(self.height):

            for j in range(len(self.arr[i])):
                gameOutline.OutlineArray[self.y+i][self.x +
                                                   j] = Fore.BLUE + Back.BLUE + self.arr[i][j]


class Brick3_red(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)

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

        # char = np.array(([[Back.BLACK + Fore.BLACK + ' ' for col in range(width)]
        #                   for row in range(height)]))
        for i in range(self.height):

            for j in range(len(self.arr[i])):
                gameOutline.OutlineArray[self.y+i][self.x +
                                                   j] = Fore.RED + Back.RED + self.arr[i][j]


red_bricks_coord = [(2, 6), (9, 6), (16, 6), (23, 6), (30, 6),
                    (37, 6), (44, 6), (51, 6), (58, 6), (65, 6), (72, 6), (79, 6)]
red_bricks_obj = []
for i in red_bricks_coord:
    red_bricks_obj.append(Brick3_red(i[0], i[1]))
for i in red_bricks_obj:
    i.generate("brick.txt")

blue_bricks_coord = [(5, 10), (12, 10), (19, 10), (26, 10), (33, 10),
                     (40, 10), (47, 10), (54, 10), (61, 10), (68, 10)]
blue_bricks_obj = []
for i in blue_bricks_coord:
    blue_bricks_obj.append(Brick2_blue(i[0], i[1]))
for i in blue_bricks_obj:
    i.generate("brick.txt")

cyan_bricks_coord = [(8, 14), (15, 14), (22, 14), (29, 14), (36, 14),
                     (43, 14), (50, 14), (57, 14), (64, 14)]
cyan_bricks_obj = []
for i in cyan_bricks_coord:
    cyan_bricks_obj.append(Brick1_cyan(i[0], i[1]))
for i in cyan_bricks_obj:
    i.generate("brick.txt")

# red_bricks_coord = [(2, 6), (9, 6), (16, 6), (23, 6), (30, 6),
#                     (37, 6), (44, 6), (51, 6), (58, 6), (65, 6)]
# red_bricks_obj = []
# for i in red_bricks_coord:
#     red_bricks_obj.append(Brick3_red(i[0], i[1]))
# for i in red_bricks_obj:
#     i.generate("brick.txt")
