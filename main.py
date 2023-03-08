# from settings import *
# from tetris import Tetris
import pygame as pg
import sys

vec=pg.math.Vector2 # define vector

FPS = 60
FIELD_COLOR = (48, 39, 32)

TILE_SIZE = 30
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_POS_OFFSET=vec(FIELD_W//2-1,0)
# INIT_POS_OFFSET=vec(FIELD_SIZE)//2
MOVE_DIRECTIONS={
    'left':vec(-1,0),'right':vec(1,0),'down':vec(0,1)
    }

TETROMINOES={
    'T':[],
    'O':[],
    'J':[],
    'L':[],
    'I':[],
    'S':[],
    'Z':[]

}

class Block:# 4 Block in sprite
    pass

# class Tetromino:# 4 Block in 1 Tetromino
    
class Tetris: # all Tetromino in the field
    def __init__(self,app):
        self.app=app

    def draw_grid(self):
        for x in range(FIELD_SIZE[0]):
            for y in range(FIELD_SIZE[1]):
                pg.draw.rect(self.app.screen,(0,0,0),(x*TILE_SIZE,y*TILE_SIZE,TILE_SIZE,TILE_SIZE),1)# 1 is for border width

    def update(self):
        pass 
    def draw(self):
        self.draw_grid()# call function inside class needs self

class App:
    def __init__(self):
        pg.init() #initial
        pg.display.set_caption('Tetris') #caption 
        self.screen = pg.display.set_mode(FIELD_RES)#set screen size
        self.clock = pg.time.Clock()# set clock
        '''game character related'''
        self.tetris=Tetris(self)# generate a new objective in initialize



    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.tetris.draw()
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:#run process
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
