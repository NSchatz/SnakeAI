from enum import Enum
import math

class Direction(Enum):
    up = 0
    down = 1
    left = 2
    right = 3

class Snake:
    length = None
    direction = None
    body = None
    block_size = None
    color = (0,0,255)
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()

    def respawn(self):
        self.length = 3
        self.body = [(120,120), (120,140), (120,160)]
        self.direction = Direction.right

    def draw(self, game, window):
        for segment in self.body:
            game.draw.rect(window, self.color, (segment[0], segment[1], self.block_size, self.block_size))

    def move(self):
        curr_head = self.body[-1]
        if self.direction == Direction.down:
            next_head = (curr_head[0], curr_head[1] + self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.up:
            next_head = (curr_head[0], curr_head[1] - self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.right:
            next_head = (curr_head[0] + self.block_size, curr_head[1])
            self.body.append(next_head)
        elif self.direction == Direction.left:
            next_head = (curr_head[0] - self.block_size, curr_head[1])
            self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    def direct(self, direction):
        if self.direction == Direction.down and direction != Direction.up:
            self.direction = direction
        elif self.direction == Direction.up and direction != Direction.down:
            self.direction = direction
        elif self.direction == Direction.left and direction != Direction.right:
            self.direction = direction
        elif self.direction == Direction.right and direction != Direction.left:
            self.direction = direction

    def eat(self):
        self.length += 1

    def check_tail_collision(self):
        head = self.body[-1]
        has_eaten_tail = False

        for i in range(len(self.body) - 1):
            segment = self.body[i]
            if head[0] == segment [0] and head[1] == segment [1]:
                has_eaten_tail = True

        return has_eaten_tail

    def check_bounds(self):
        head = self.body[-1]
        if head[0] >= self.bounds[0]+100:
            return True
        if head[1] >= self.bounds[1]+100:
            return True

        if head[0] < 100:
            return True
        if head[1] < 100:
            return True

        return False

    def check_for_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            food.respawn()
    def distance_to_food(self, food):
        head = self.body[-1]
        x = (food.x - head[0])**2/20
        y = (food.y - head[1])**2/20
        c = math.sqrt(x + y)
        print(c)
