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

    def changescore(self, deleted):
        '''changes the score'''
        if deleted == 'coin':
            self.score += 10

        if deleted == 'enemy':
            self.score += 100

        if deleted == 'boss':
            self.score += 500

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
