#from bricks import *
from manage import *
#from playsound import playsound
#from powerups import *

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
        Ballobj.lifelost = 1


    # need some fine tuning for X direction/vel etc. not proper.
    if ((Ballobj.x + Ballobj.vel_x <= -1) or (Ballobj.x + Ballobj.vel_x >= 100)):
        Ballobj.vel_x *= -1


def collision_brick(Ballobj, Bricks_obj, bricktype):
    #in the fllowing i.height doesnt matter as the height is just 1. written just for generalization

    for i in Bricks_obj:
        if ((Ballobj.y + Ballobj.vel_y == i.y + i.height - 1) or (Ballobj.y + Ballobj.vel_y == i.y)):
            if (Ballobj.x in [j for j in range(i.x - abs(Ballobj.vel_x), i.x + i.width + abs(Ballobj.vel_x))]):
                Ballobj.vel_y *= -1
                if (((Ballobj.vel_x > 0) and (Ballobj.x + Ballobj.vel_x == i.x)) or ((Ballobj.vel_x < 0) and (Ballobj.x + Ballobj.vel_x == i.x + i.width - 1))):
                    Ballobj.vel_x *= -1
                if(bricktype != "unbreakable"):
                    i.clearbrick(i, bricktype)
                    i.changebrick(i, bricktype)
        elif (Ballobj.y == i.y):
            if (((Ballobj.vel_x < 0) and (Ballobj.x == i.x + i.width)) or ((Ballobj.vel_x > 0) and (Ballobj.x == i.x - 1))):
                Ballobj.vel_x *= -1
                if(bricktype != "unbreakable"):
                    i.clearbrick(i, bricktype)
                    i.changebrick(i, bricktype)


def collision_pow(Powerobj, Paddleobj, powertype):
    if (Powerobj.y + Powerobj.vel_y == 29):
        if (Powerobj.x in range(Paddleobj.x + Paddleobj.width)):
            Powerobj.clearPower(Powerobj, powertype)
            Powerobj.activate(Powerobj, Paddleobj, powertype)
