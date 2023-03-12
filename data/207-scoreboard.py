import pygame as pg 
from ship import Ship
# import pygame.font

class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = 0
        self.game = game
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = game.stats
        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()
        self.prep_ships()

    def increment_score(self, key, point=0): 
        if key == 0:
            val = self.settings.pink_alien
        elif key == 1:
            val = self.settings.blue_alien
        elif key == 2:
            val = self.settings.green_alien
        else:
            val = point
        self.score += val
        self.prep_score()

    def prep_ships(self):
        self.ships = []
        for ship_number in range(self.game.ship.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.append(ship)


    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def reset(self): 
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)
        if self.stats.game_active:
            for ship in self.ships:
                ship.draw()