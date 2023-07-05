import pygame as py
from engine.game_objects.game_object import GameObject


class Projectile(GameObject):

    def __init__(self, pos, game):
        super(Projectile, self).__init__('all_sprites', game)
        self.pos = pos
        self.image = py.image.load(self.game.imgDir+'\\bullet.png')
        self.rect = self.image.get_rect(center=self.pos)
        self.move_speed = 300

    def calculate_movement(self, amount):
        if amount == 0:
            return 0
        if self.game.fps == 0:
            return 0
        return amount/(self.game.fps/self.move_speed)

    def move(self, y):
        self.rect.move_ip(0, self.calculate_movement(y))

    def update(self):
        self.move(-1)
        self.pos = self.rect.center
        if self.pos[1] < -100:
            self.game.objects.pop(self.object_key)
        elif self.pos[1] > 900:
            self.game.objects.pop(self.object_key)