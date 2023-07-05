import pygame as py
from engine.game_objects.game_object import IGameObject
from engine.game_objects.modules import ICollisionModule
from engine.game_objects.modules import IControlModule
from engine.game_objects.modules import IAnimationModule
from engine.image.sprite_sheet import SpriteSheet


# Player Object #
class Player(IGameObject):
    def __init__(self, pos, game):
        super(Player, self).__init__('player', game)
        self.set_module("collision", ICollisionModule(self, callback=self.callback_on_collision))
        self.get_module("collision").collision_groups = ["enemy"]
        self.modules["control"] = IControlModule(self, callback=self.callback_input_tick)
        self.modules["animation"] = IAnimationModule(self)

        self.pos = pos
        self.last_pos = (0, 0)
        self.sprite_sheet = SpriteSheet(f"{self.game.imgDir}\\ship_00.png", 66, 38).get_image_array()
        self.image = self.sprite_sheet[0]
        self.rect = self.image.get_rect(center=self.pos)
        self.modules["animation"].add_animation_by_dict("engines_on",
            {
                "frames": [self.sprite_sheet[1]],
                "frame_time": 500,
                "loop": False,
            }
        )
        self.modules["animation"].should_animate = True
        self.debug = True

    def callback_on_collision(self, obj, group): print(f"hit: {obj} - {group}")

    def callback_input_tick(self):
        self.last_pos = self.pos
        self.pos = self.modules["control"].get_mouse_pos()

    def update(self):
        if self.last_pos != self.pos:
            self.modules["animation"].play("engines_on")
        else:
            if self.modules["animation"].active_anim == None:
                self.image = self.sprite_sheet[0]
                
        self.rect = self.image.get_rect(center=self.pos)
        super(Player, self).update()
