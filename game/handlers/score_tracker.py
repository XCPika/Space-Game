from engine.game_objects.game_object import GameObject

# Score Tracker #

class ScoreTracker(GameObject):
    def __init__(self, game):
        super(ScoreTracker, self).__init__('none', game)
        self.score = 0
        self.debug = False

    def update_score(self, amount): self.score += amount
