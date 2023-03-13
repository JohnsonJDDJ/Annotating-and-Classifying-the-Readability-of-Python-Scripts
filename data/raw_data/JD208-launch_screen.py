import pygame as pg

class Launch:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.images = []
        self.default_color = (255, 255, 255)
        self.prep_strings()
        self.prep_aliens()

    
    def prep_strings(self):
        self.prep_Text("SPACE", 170, offsetY=40)
        self.prep_Text("INVADERS", 90, color=(0,210,0), offsetY=140)
        self.prep_Text("= 10 PTS", 40, offsetX=600, offsetY=300)
        self.prep_Text("= 20 PTS", 40, offsetX=600, offsetY=350)
        self.prep_Text("= 40 PTS", 40, offsetX=600, offsetY=400)
        self.prep_Text("= ???", 40, offsetX=610, offsetY=450)
    
    def prep_aliens(self):
        alien1 = pg.transform.rotozoom(pg.image.load(f'images/alien_03-0.png'), 0, 1.5)
        self.images.append((alien1, (540, 290)))
        alien1 = pg.transform.rotozoom(pg.image.load(f'images/alien__10.png'), 0, .5)
        self.images.append((alien1, (525, 340)))
        alien1 = pg.transform.rotozoom(pg.image.load(f'images/alien__20.png'), 0, .5)
        self.images.append((alien1, (525, 390)))
        alien1 = pg.transform.rotozoom(pg.image.load(f'images/ufo.png'), 0, 1.2)
        self.images.append((alien1, (500, 410)))

    def prep_Text(self, msg, size, color=(255,255,255), offsetX=0, offsetY=0):
        font = pg.font.SysFont(None, size)
        text_image = font.render(msg, True, color, self.settings.bg_color)
        rect = text_image.get_rect()
        if offsetY == 0:
            rect.centery = self.screen_rect.centery
        else:
            rect.top = offsetY
        if offsetX == 0:
            rect.centerx = self.screen_rect.centerx
        else:
            rect.left = offsetX

        self.images.append((text_image,rect))

    def draw(self):
        for image in self.images:
            self.screen.blit(image[0], image[1])