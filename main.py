from items import *
from bricks import *
from outline import gameOutline
from manage import *
import time
import signal
import sys
import numpy as np
import getch
from os import system
from time import sleep
import colorama
from colorama import *
colorama.init(autoreset=True)
#from colorama import Fore, Back, Style
# Paddleobj.generatePaddle()
gameOutline.display()


TIMEOUT = 0.1  # number of seconds your want for timeout


def interrupted(signum, frame):
    # "called when read times out"
    # print('interrupted!')
    pass


#signal.signal(signal.SIGALRM, interrupted)


def user_input():
    try:

        signal.signal(signal.SIGALRM, interrupted)
        signal.setitimer(signal.ITIMER_REAL, TIMEOUT)
        #print('You have 0.1 seconds to type in your stuff...')
        foo = getch.getch()
        # disable the alarm after success
        signal.alarm(0)
        return foo
    except:
        # timeout
        return ''  # ' ' will return space - verified by printing ord(char)


start_time = time.time()
while (1):
    system('tput reset')

    gameOutline.display()
    Manager.generatehead()

    # enable the alarm
    #signal.setitimer(signal.ITIMER_REAL, TIMEOUT)
    # signal.alarm(TIMEOUT)

    char = user_input()

    if char == 'q':
        break
    elif char == 'j' or char == 'l':
        Paddleobj.move(char)

    # if ballobj.move is always executed then say if we keep pressing j to move paddle faster, the ball also travels faster
    # to handle that we use elapsed time concept. thus ball moves every 0.1 s not less than that
    # below thing working erratically. ballobj,move getting called suspiciouslly have to keep pressing space
    elapsed_time = time.time() - start_time
    if(elapsed_time >= TIMEOUT):
        Ballobj.move(char)
        start_time = time.time()
    #signal.signal(signal.SIGALRM, signal.SIG_IGN)


# while 1:
#     system('tput reset')
#     gameOutline.display()

#     char = user_input()
#     if char == 'j' or char == 'l':
#         Paddleobj.move(char)
#     else:
#         break
