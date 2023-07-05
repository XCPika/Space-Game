import pygame as py
from engine.game_engine import Pygame
from engine.color import Color
from os import path
from game.actors.player import Player
from game.ui.fps_text import FPSText
from engine.map.looping_map import LoopingMap


# Main Game Engine Object #
class Game(Pygame):
    def __init__(self):
        super(Game, self).__init__(1280, 720, "Space Game", fps_target=60)
        self.groups["enemy"], self.groups["map"], self.groups["player"] = py.sprite.Group(), py.sprite.Group(), py.sprite.Group()
        # self.axis = {'move_left': {py.K_a: -1, py.K_d: 1}, 'move_up': {py.K_w: -1, py.K_s: 1}}
        self.load_data()
        self.loop()

    def load_data(self):
        super(Game, self).load_data()
        self.imgDir = path.join(self.gameDir, 'data\\images')
        self.map_dir = path.join(self.gameDir, 'data\\maps')
        self.fonts["pixelplay"] = self.get_font("pixelplay")
        self.fonts["i_pixel_u"] = self.get_font("i_pixel_u")
        self.objects['map'] = LoopingMap(self, "background.png")
        self.objects['player'] = Player((self.windowSize[0] / 2, self.windowSize[1] / 2), self)
        self.objects['fps'] = FPSText((500, 100), self)

    def draw(self):
        self.screen.fill(Color(1, 1, 1, 1).RGB)
        super(Game, self).draw()
        for group in self.groups.keys():
            for sprite in self.groups[group]:
                if self.debug:
                    if sprite.debug:
                        py.draw.rect(py.display.get_surface(), Color(1, 0, 0, 1).RGBA, sprite.rect, 1)
        super(Game, self).render_display()

    def update(self):
        super(Game, self).update()
        for event in py.event.get():
            if event.type == py.VIDEORESIZE:
                self.windowSize = (event.w, event.h)
                py.display._resize_event(event)
            if event.type == py.QUIT:
                self.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_c:
                    self.debug = not self.debug
                if event.key == py.K_ESCAPE:
                    self.quit()

    def loop(self):
        while self.running:
            self.update()
            self.draw()


g = Game()
