import os
import time


class Manage():
    def __init__(self):
        self.score = 0
        self.lives = 3

    def generatehead(self):
        '''prints the header'''
        print("")
        print("YOUR SCORE IS : " + str(self.score) +
              "\t\t\t\t\t\t      LIVES LEFT : " + str(self.lives))
        print("")

    def changescore(self, points):
        '''changes the score'''
        self.score += points

    def changelives(self):
        time.sleep(1)
        if self.lives == 0:
            os.system("tput reset")
            print('GAME OVER')
            print('Your Final Score is : ' + str(self.score))
            print('')
            exit()
        else:
            self.lives -= 1


Manager = Manage()
