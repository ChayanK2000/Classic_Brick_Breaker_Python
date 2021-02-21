import os
import time


class Manage():
    def __init__(self):
        self.score = 0
        self.time_taken = 0
        self.lives = 3

    def generatefoot(self):

        print("")
        print("YOUR SCORE IS : " + str(self.score) +
              "\t\t\t TIME: "+str(self.time_taken) + "\t\t\t  LIVES LEFT : " + str(self.lives))
        print("")

    def changescore(self, points):
        '''changes the score'''
        self.score += points

    def change_time(self):
        self.time_taken += 1

    def changelives(self):
        time.sleep(1)
        if self.lives == 1:  # 0 or 1 depending on understanding
            #os.system("tput reset")
            print('---------------------------\n')
            print('GAME OVER')
            print('Your Final Score is : ' + str(self.score))
            print('Total time taken: ' + str(self.time_taken))
            print('')
            exit()
        else:
            self.lives -= 1


Manager = Manage()
