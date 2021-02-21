import numpy as np
import colorama
from colorama import *
colorama.init(autoreset=True)

left2 = np.array([8, 90])
left2 = np.append(left2, 8)
left2 = np.append(left2, 9)
left2 = left2 + 1
print(left2)

left1 = [1, 2, 3, 4]
left1 = np.array(left1)
left1 += 1
print(left1)


def hi():
    global x
    x = 10


global x
x = 5
hi()
print(x)
forecolour = Fore.YELLOW
print(forecolour + "yo")
