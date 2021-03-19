from outline import gameOutline
from super_items import *
import colorama
from colorama import *
colorama.init(autoreset=True)


class PowerUp(Item):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        # self.x = x
        # self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.history = 0

    def move(self):
        self.vel_y = 1

        if (self.history == 0):
            for i in range(0, self.height):
                for j in range(0, len(self.arr[i])):
                    gameOutline.OutlineArray[self.y + i][self.x +
                                                         j] = Fore.BLACK + Back.BLACK + " "

            self.history = 0
            self.x += self.vel_x
            self.y += self.vel_y

            if (gameOutline.OutlineArray[self.y][self.x] != Fore.BLACK + Back.BLACK + " "):
                self.history = 1
            else:
                for i in range(0, self.height):
                    for j in range(0, len(self.arr[i])):
                        gameOutline.OutlineArray[self.y + i][self.x +
                                                             j] = Fore.GREEN + Back.BLACK + self.arr[i][j]


class Expand_Paddle(PowerUp):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)


exp_paddle_pow_coord = [(24, 14), (21, 10)]
exp_paddle_pow_obj = []
# this dict works as the boolean for whether the powerup is detached(the brick containing it is cleared) or not
exp_paddle_pow_dict = {}
for i in exp_paddle_pow_coord:
    exp_paddle_pow_obj.append(Expand_Paddle(
        i[0], i[1], "power_expand.txt", Fore.GREEN, Back.BLACK))
for i in exp_paddle_pow_obj:
    exp_paddle_pow_dict[i] = 0
    # i.generate("power_expand.txt")
