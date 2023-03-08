class App:
    def __init__(self):
        '''game character related'''
        self.tetris=Tetris(self)#
    def draw(self):
        self.tetris.draw_grid()

class Tetris: # all Tetromino in the field
    def __init__(self,app):
        self.app=app
    def draw_grid(self):
        print(self.app)

char_a=App()
char_a.draw()

