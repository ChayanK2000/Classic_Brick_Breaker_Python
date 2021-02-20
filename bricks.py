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

    def clearbrick(self, Brick_obj):
        for i in range(Brick_obj.height):

            for j in range(len(Brick_obj.arr[i])):
                gameOutline.OutlineArray[Brick_obj.y+i][Brick_obj.x +
                                                        j] = Fore.BLACK + Back.BLACK + " "


class Brick1(Brick):
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


red_bricks_coord = [(2, 2), (9, 2), (16, 2), (23, 2), (30, 2),
                    (37, 2), (44, 2), (51, 2), (58, 2), (65, 2)]
red_bricks_obj = []
for i in red_bricks_coord:
    red_bricks_obj.append(Brick1(i[0], i[1]))
for i in red_bricks_obj:
    i.generate("brick.txt")
# red1 = Brick1(2, 2)
# red2 = Brick1(7, 2)
# red3 = Brick1(12, 2)
# red4 = Brick1(17, 2)
# red5 = Brick1(22, 2)
# red6 = Brick1(27, 2)
# red7 = Brick1(32, 2)
# red8 = Brick1(37, 2)
# red9 = Brick1(42, 2)
# red10 = Brick1(47, 2)
