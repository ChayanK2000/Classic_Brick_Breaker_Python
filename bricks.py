from manage import Manager
from outline import gameOutline
from powerups import *
from super_items import *
import colorama
from colorama import *
from collections import defaultdict
from random import randint

# from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

# using dfs to first store all explosive brick in contact with another explosive brick
# using python dictionary to act as adjacency list
global arrtoexplode
adj = defaultdict(list)
visited = set()
arrtoexplode = []

# inheritance + polymorphism


class Brick(Item):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        self.strength = 1
        self.worth = 0
        self.hitbyfireball = 0


    def evaluate(self, Brick_obj):
        Manager.changescore(Brick_obj.worth)

           #following code because the powerups come own only after brick is cleared(i,e, when cyan is hit)
        if ((Brick_obj.x + 2, Brick_obj.y) in exp_paddle_pow_coord):
            ind = exp_paddle_pow_coord.index(
                (Brick_obj.x + 2, Brick_obj.y))
            exp_paddle_pow_obj[ind].generate(
                "power_expand.txt", Fore.GREEN, Back.BLACK)
            exp_paddle_pow_dict[exp_paddle_pow_obj[ind]] = 1

        if ((Brick_obj.x + 2, Brick_obj.y) in fireball_pow_coord):
            ind = fireball_pow_coord.index(
                (Brick_obj.x + 2, Brick_obj.y))
            fireball_pow_obj[ind].generate(
                "power_fireball.txt", Fore.LIGHTRED_EX, Back.BLACK)
            fireball_pow_dict[fireball_pow_obj[ind]] = 1

    def handleexplosives(self, Brick_obj):  # only to handle explosive cases
        for i in range(Brick_obj.height):

            for j in range(len(Brick_obj.arr[i])):
                gameOutline.OutlineArray[Brick_obj.y+i][Brick_obj.x +
                                                        j] = Fore.BLACK + Back.BLACK + " "
        ref_x = Brick_obj.x
        ref_y = Brick_obj.y
        for i_y in range(ref_y - 1, ref_y + 2):
            for j_x in range(ref_x - 6, ref_x + 7):
                if((i_y in range(0, 30)) and (j_x in range(0, 99))): #these conditions so that due to range of outer loops, we dont get out of the scene of game
                    if ((j_x, i_y) in red_bricks_coord):
                        ind = red_bricks_coord.index((j_x, i_y))
                        objjj = red_bricks_obj[ind]
                        self.clearbrick(objjj, "red")
                        Manager.changescore(objjj.worth)
                    if ((j_x, i_y) in blue_bricks_coord):
                        ind = blue_bricks_coord.index((j_x, i_y))
                        objjj = blue_bricks_obj[ind]
                        self.clearbrick(objjj, "blue")
                        Manager.changescore(objjj.worth)
                    if ((j_x, i_y) in cyan_bricks_coord):
                        ind = cyan_bricks_coord.index((j_x, i_y))
                        objjj = cyan_bricks_obj[ind]
                        self.clearbrick(objjj, "cyan")
                        Manager.changescore(objjj.worth)
                    if ((j_x, i_y) in unbreak_bricks_coord):
                        ind = unbreak_bricks_coord.index((j_x, i_y))
                        objjj = unbreak_bricks_obj[ind]
                        self.clearbrick(objjj, "unbreakable")

    def clearbrick(self, Brick_obj, bricktype):
        

        for i in range(Brick_obj.height):

            for j in range(len(Brick_obj.arr[i])):
                gameOutline.OutlineArray[Brick_obj.y+i][Brick_obj.x +
                                                        j] = Fore.BLACK + Back.BLACK + " "
        
        if (bricktype == "explosive"):
            # to accomodate for the fact when multiple clusters/bricks(explosives) are not joined together
            global arrtoexplode

            dfs(visited, adj, Brick_obj)
            for i in arrtoexplode:
                expl_bricks_coord.remove((i.x, i.y))
                expl_bricks_obj.remove(i)
                self.handleexplosives(i)
            arrtoexplode = []

        elif (bricktype == "rainbow"):
            rainbow_bricks_coord.remove((Brick_obj.x, Brick_obj.y))
            rainbow_bricks_obj.pop((Brick_obj.x, Brick_obj.y))

        elif (Brick_obj.hitbyfireball == 1):
            Brick_obj.hitbyfireball = 0
            self.handleexplosives(Brick_obj)        
            

        

        elif (bricktype == "red"):
            red_bricks_coord.remove((Brick_obj.x, Brick_obj.y))
            red_bricks_obj.remove(Brick_obj)
        elif (bricktype == "blue"):
            blue_bricks_coord.remove((Brick_obj.x, Brick_obj.y))
            blue_bricks_obj.remove(Brick_obj)
        elif (bricktype == "cyan"):
            cyan_bricks_coord.remove((Brick_obj.x, Brick_obj.y))
            cyan_bricks_obj.remove(Brick_obj)

        elif (bricktype == "unbreakable"):
            unbreak_bricks_coord.remove((Brick_obj.x, Brick_obj.y))
            unbreak_bricks_obj.remove(Brick_obj)
        


    def changebrick(self, Brick_obj, bricktype, Ballobj):
        
        
        if (bricktype == "rainbow"):
            color = randint(0, 2)
            if color == 0:
                objjj = Brick1_cyan(Brick_obj.x, Brick_obj.y,
                                    "brick.txt", Fore.CYAN, Back.CYAN)
                cyan_bricks_coord.append((Brick_obj.x, Brick_obj.y))
                cyan_bricks_obj.append(objjj)
            elif color == 1:
                objjj = Brick2_blue(Brick_obj.x, Brick_obj.y,
                                    "brick.txt", Fore.BLUE, Back.BLUE)
                blue_bricks_coord.append((Brick_obj.x, Brick_obj.y))
                blue_bricks_obj.append(objjj)
            elif color == 2:
                objjj = Brick3_red(Brick_obj.x, Brick_obj.y,
                                    "brick.txt", Fore.RED, Back.RED)
                red_bricks_coord.append((Brick_obj.x, Brick_obj.y))
                red_bricks_obj.append(objjj)

        elif (Ballobj.fire == 1):
            self.evaluate(Brick_obj)
            return

        elif (bricktype == "red"):

            objjj = Brick2_blue(Brick_obj.x, Brick_obj.y,
                                "brick.txt", Fore.BLUE, Back.BLUE)
            objjj.worth = Brick_obj.worth  # to keep worth of original brick
            blue_bricks_coord.append((Brick_obj.x, Brick_obj.y))
            blue_bricks_obj.append(objjj)
            #objjj.generate("brick.txt", Fore.BLUE, Back.BLUE)
        elif (bricktype == "blue"):
            objjj = Brick1_cyan(Brick_obj.x, Brick_obj.y,
                                "brick.txt", Fore.CYAN, Back.CYAN)
            objjj.worth = Brick_obj.worth
            cyan_bricks_coord.append((Brick_obj.x, Brick_obj.y))
            cyan_bricks_obj.append(objjj)
            #objjj.generate("brick.txt", Fore.CYAN, Back.CYAN)
        elif (bricktype == "cyan"):
            self.evaluate(Brick_obj)


class Brick1_cyan(Brick):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        self.worth = 10


class Brick2_blue(Brick):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        self.worth = 20

class Brick3_red(Brick):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        self.worth = 30


class Brick4_unbreak(Brick):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        self.unbreak = 1


class Brick5_expl(Brick):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)
        # self.worth = 5


class Brick6_rainbow(Brick):
    def __init__(self, x, y, path, forecolour, backcolour):
        super().__init__(x, y, path, forecolour, backcolour)


# initializing all bricks with cordinates and their objects. Each brick has an object.
red_bricks_coord = [(23, 4), (61, 10), (37, 4), (44, 4),
                    (36, 14), (58, 4), (65, 4), (71, 14), (71,11)]
red_bricks_obj = []
for i in red_bricks_coord:
    red_bricks_obj.append(Brick3_red(
        i[0], i[1], "brick.txt", Fore.RED, Back.RED))
# for i in red_bricks_obj:
#     i.generate("brick.txt")

blue_bricks_coord = [(30, 4), (12, 10), (19, 10), (26, 10), (33, 10),
                     (40, 10), (47, 10), (54, 10), (68, 10), (75, 10), (77,11)]
blue_bricks_obj = []
for i in blue_bricks_coord:
    blue_bricks_obj.append(Brick2_blue(
        i[0], i[1], "brick.txt", Fore.BLUE, Back.BLUE))
# for i in blue_bricks_obj:
#     i.generate("brick.txt")

cyan_bricks_coord = [(22, 14), (29, 14), (51, 4),
                     (43, 14), (50, 14), (57, 14), (64, 14), (72, 4), (78, 14)]
cyan_bricks_obj = []
for i in cyan_bricks_coord:
    cyan_bricks_obj.append(Brick1_cyan(
        i[0], i[1], "brick.txt", Fore.CYAN, Back.CYAN))
# for i in cyan_bricks_obj:
#     i.generate("brick.txt")

unbreak_bricks_coord = [(23, 6), (30, 6),
                        (37, 6), (44, 6), (51, 6), (58, 6), (65, 6), (72, 6)]
unbreak_bricks_obj = []
for i in unbreak_bricks_coord:
    unbreak_bricks_obj.append(Brick4_unbreak(
        i[0], i[1], "brick.txt", Fore.WHITE, Back.WHITE))
# for i in unbreak_bricks_obj:
#     i.generate("brick.txt")

expl_bricks_coord = [(8, 3), (14, 4), (20, 5), (26, 5), (32, 5), (38, 5),
                     (44, 5), (50, 5), (56, 5), (62, 5), (68, 5), (74, 5), (80, 5), (86, 6), (92,7), (50,20), (56,20)]
expl_bricks_obj = []
for i in expl_bricks_coord:
    expl_bricks_obj.append(Brick5_expl(
        i[0], i[1], "exploding_brick.txt", Fore.BLACK, Back.YELLOW))
# for i in expl_bricks_obj:
#     i.generate("exploding_brick.txt")

for i in expl_bricks_obj:
    for j in expl_bricks_obj:
        if (((abs(i.x - j.x)) <= 6) and ((abs(i.y - j.y)) <= 1)):
            adj[j].append(i)
            adj[i].append(j)

# dfs only for exploding bricks handling
def dfs(visited, adj, node):
    if node not in visited:
        arrtoexplode.append(node)
        visited.add(node)
        for neighbour in adj[node]:
            dfs(visited, adj, neighbour)


rainbow_bricks_coord = [(35,20),(72,7)]
rainbow_bricks_obj = {}
rainbow_colours = [(Fore.CYAN, Back.CYAN), (Fore.BLUE,
                                            Back.BLUE), (Fore.RED, Back.RED)]

