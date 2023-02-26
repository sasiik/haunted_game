from vars import *


class AnimatedObject:
    def __init__(self, x, y, animation, scale):
        self.width = animation[0].get_width()
        self.height = animation[0].get_height()
        self.anim = animation
        self.scaling(scale)
        self.rect = self.anim[0].get_rect()
        self.rect.topleft = (x, y)

    def draw(self, frame):
        screen.blit(self.anim[frame], (self.rect.x, self.rect.y))

    def scaling(self, scale):
        if scale != (1, 1):
            for i in range(len(self.anim)):
                self.anim[i] = pygame.transform.scale(self.anim[i],
                                                      (int(self.width * scale[0]), int(self.height * scale[1])))
