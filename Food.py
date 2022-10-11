from random import randint
class Food:
    x = None
    y = None
    block_size = None
    color = (0,255,0)

    def __init__(self, block_size):
        self.block_size = block_size
        self.respawn()

    def respawn(self):
        self.x = randint(5,24)*20
        self.y = randint(5,24)*20

    def draw(self, game, window, body):
        fruit = game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size ))
        if any(fruit.collidepoint(*pos) for pos in body): 
            self.respawn()

        
