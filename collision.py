from bricks import *
from manage import *


def collision_paddle(Ballobj, Paddleobj):
    if (Ballobj.y + Ballobj.vel_y == 29):
        # print(Paddleobj.left2)
        # print(Paddleobj.left1)
        # print(Paddleobj.centre)
        # print(Paddleobj.right1)
        # print(Paddleobj.right2)
        # exit()
        # -1 and +1 at start and end so that ball bounces even at the corners
        if (Ballobj.x in Paddleobj.left2):
            Ballobj.vel_x += -2
            Ballobj.vel_y *= -1
        # following if for the point left of starting
        elif ((Ballobj.x == Paddleobj.x - 1) and (Ballobj.vel_x >= 0)):
            Ballobj.vel_x += -2
            Ballobj.vel_y *= -1
        elif (Ballobj.x in Paddleobj.left1):
            Ballobj.vel_x += -1
            Ballobj.vel_y *= -1
        elif (Ballobj.x in Paddleobj.centre):
            Ballobj.vel_x += 0
            Ballobj.vel_y *= -1
        elif (Ballobj.x in Paddleobj.right1):
            Ballobj.vel_x += 1
            Ballobj.vel_y *= -1
        elif (Ballobj.x in Paddleobj.right2):
            Ballobj.vel_x += 2
            Ballobj.vel_y *= -1
        # following if for point right of end
        elif ((Ballobj.x == Paddleobj.x + Paddleobj.width) and (Ballobj.vel_x <= 0)):
            Ballobj.vel_x += 2
            Ballobj.vel_y *= -1


def collision_wall(Ballobj, Paddleobj):
    if ((Ballobj.y + Ballobj.vel_y <= -1)):
        Ballobj.vel_y *= -1
    if (Ballobj.y + Ballobj.vel_y == 30):
        Manager.changelives()
        # basically any object of item class instead of ballobj
        Ballobj.clearOnLiveLost(Paddleobj)
        # basically any object of item class instead of ballobj
        Ballobj.clearOnLiveLost(Ballobj)

        # on trying to do below code and remove from items.py, strangely on losing a life i cant release the ball, no matter how much time space is pressed.
        # re initializing and generating like at the start
        # Ballobj.lifelost = True
        # Paddleobj.x = 40
        # Paddleobj.y = 29
        # Ballobj.x = 49
        # Ballobj.y = 28
        # Ballobj.vel_x, Ballobj.vel_y = 0, 0
        # Ballobj.rest = True
        # Paddleobj.generate('paddle.txt')
        # Ballobj.generate('ball1.txt')

    # need some fine tuning for X direction/vel etc. not proper.
    if ((Ballobj.x + Ballobj.vel_x <= -1) or (Ballobj.x + Ballobj.vel_x >= 100)):
        Ballobj.vel_x *= -1


def collision_brick(Ballobj, Bricks_obj, bricktype):
    # need to do dame fine tuning. like it is almost correct except at very high speeds.
    for i in Bricks_obj:
        if (Ballobj.y + Ballobj.vel_y == i.y):
            if (Ballobj.x in [j for j in range(i.x, i.x + i.width)]):
                Ballobj.vel_y *= -1
                if(bricktype != "unbreakable"):
                    i.clearbrick(i, bricktype)
                    i.changebrick(i, bricktype)
                    # if (bricktype == 'cyan'):
                    #     # for powerups
                    #     if ((i.x + 2, i.y) in exp_paddle_coord):
                    #         ind = exp_paddle_coord.index(
                    #             (i.x + 2, i.y))
                    #         exp_paddle_obj[ind].generate("power_expand.txt")

        if (Ballobj.x + Ballobj.vel_x == i.x):
            if (Ballobj.y in [j for j in range(i.y, i.y + i.height)]):
                Ballobj.vel_x *= -1
                if(bricktype != "unbreakable"):
                    i.clearbrick(i, bricktype)
                    i.changebrick(i, bricktype)

        # elif to handle the four corners only if above two dont satisfy
        if (((Ballobj.y + Ballobj.vel_y == i.y) and (Ballobj.x + Ballobj.vel_x == i.x)) or ((Ballobj.y + Ballobj.vel_y == i.y + i.height - 1) and (Ballobj.x + Ballobj.vel_x == i.x + i.width - 1))):
            Ballobj.vel_x *= -1
            Ballobj.vel_y *= -1
            if(bricktype != "unbreakable"):
                i.clearbrick(i, bricktype)
                i.changebrick(i, bricktype)
