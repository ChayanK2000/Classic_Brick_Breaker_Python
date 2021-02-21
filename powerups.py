

class PowerUp():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Expand_Paddle(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)


exp_paddle_coord = [(24, 14)]
exp_paddle_obj = []
for i in exp_paddle_coord:
    exp_paddle_obj.append(Expand_Paddle(i[0], i[1]))
for i in exp_paddle_obj:
    i.generate
