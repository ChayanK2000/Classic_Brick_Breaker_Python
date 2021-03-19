from outline import gameOutline
from super_items import *
#from items import Paddleobj
import colorama
from colorama import *
from collision import *
colorama.init(autoreset=True)


class PowerUp(Item):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        # self.x = x
        # self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.init_x = x
        self.init_y = y
        self.history = 0
        self.powlost = 0
        self.rest = True
        self.time = 0

    def move(self, Powerobj, Paddleobj, Ballobj, powertype):
        if (self.rest == True):
            self.vel_y = Ballobj.prev_vel_y
            self.vel_x = Ballobj.prev_vel_x
            self.rest = False
            self.time += 1

        self.time += 1
        
        if (self.history == 0):
            for i in range(0, self.height):
                for j in range(0, len(self.arr[i])):
                    gameOutline.OutlineArray[self.y + i][self.x +
                                                         j] = Fore.BLACK + Back.BLACK + " "
        if (self.time >= 5):
            self.vel_y += 1
            self.time = 0
        collision_pow(Powerobj, Paddleobj,Ballobj, powertype)
        collision_pow_wall(Powerobj, powertype)
        if (Powerobj.powlost == 1):
            return

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

    def clearPower(self, Powerobj, powertype):
        for i in range(Powerobj.height):

            for j in range(len(Powerobj.arr[i])):
                gameOutline.OutlineArray[Powerobj.y+i][Powerobj.x +
                                                        j] = Fore.BLACK + Back.BLACK + " "
        
        if (powertype == "expand"):
            exp_paddle_pow_coord.remove((Powerobj.init_x, Powerobj.init_y))
            exp_paddle_pow_obj.remove(Powerobj)

        if (powertype == "fireball"):
            fireball_pow_coord.remove((Powerobj.init_x, Powerobj.init_y))
            fireball_pow_obj.remove(Powerobj)

    def activate(self, Powerobj, Paddleobj,Ballobj, powertype):
        if (powertype == "expand"):
            Paddleobj.x -= 2 
            Paddleobj.generate('expanded_paddle.txt', Fore.GREEN, Back.BLACK)
            Paddleobj.partitions()

        if (powertype == "fireball"):
            Ballobj.fire = 1
            Ballobj.generate('ball1.txt', Fore.RED, Back.BLACK)



class Expand_Paddle(PowerUp):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)


class Fireball(PowerUp):
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

fireball_pow_coord = [(73,14)]
fireball_pow_obj = []
# this dict works as the boolean for whether the powerup is detached(the brick containing it is cleared) or not
fireball_pow_dict = {}
for i in fireball_pow_coord:
    fireball_pow_obj.append(Fireball(
        i[0], i[1], "power_fireball.txt", Fore.GREEN, Back.BLACK))
for i in fireball_pow_obj:
    fireball_pow_dict[i] = 0



