from os import system
import numpy as np
import colorama
from colorama import *
colorama.init(autoreset=True)
#from colorama import init, Fore, Back, Style


class Outline:
    def __init__(self):
        #self.OutlineArray = [[] for i in range(0, 32)]
        # to have colored characters in array, the initialized array should have color. or else append should be used
        self.OutlineArray = np.array(([[Fore.BLACK + Back.BLACK + ' ' for col in range(0, 100)]
                                       for row in range(0, 32)]))
        # for i in range(0, 32):
        #     for j in range(0, 100):
        #         self.OutlineArray[i].append(' ')

    def display(self):
        system("tput reset")
        disp = ""
        for i in range(0, 32):
            for j in range(0, 100):
                #print(self.OutlineArray[i][j], end="")
                disp += self.OutlineArray[i][j]
            # print()
            disp += "\n"
        print(disp)
        # system('clear')


gameOutline = Outline()
