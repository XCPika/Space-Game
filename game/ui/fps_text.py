from engine.ui.text import Text
from engine.color import Color


class FPSText(Text):
    def __init__(self, pos, game):
        super(FPSText, self).__init__("", Color(1, 1, 1, 1).RGB, pos=pos, game=game)

    def update(self): self.update_text(str(self.game.fps))
