import numpy as np

from py5 import Sketch
from random import random


class Worm:
    def __init__(self, pos, app):
        self.x, self.y = pos
        self.radius = 1
        self.length = 1.7
        self.angle = random() * np.pi * 2
        self.app = app

    def draw(self):
        if self.radius > 0:
            if self.app.num_iter < self.app.max_iter:
                self.app.circle(self.x, self.y, self.radius)

                self.angle += self.app.noise(0.1 * (self.x + self.app.num_iter),
                                             0.1 * self.y) * 2 * np.pi - np.pi

                self.x += np.cos(self.angle) * self.length
                self.y += np.sin(self.angle) * self.length

                if self.app.num_iter < self.app.max_iter / 2:
                    self.radius += 0.02
                else:
                    self.radius -= 0.02

                self.radius = max(1, min(3, self.radius))


class App(Sketch):
    def __init__(self, width, height, max_iter):
        super().__init__()
        self.num_iter = 0

        self.canvas_size = width, height
        self.max_iter = max_iter

        self.worms = []
        for x in range(0, width, 50):
            for y in range(0, height, 50):
                self.worms.append(Worm((x, y), self))

    def settings(self):
        self.size(*self.canvas_size)

    def setup(self):
        self.rect_mode(self.CORNERS)
        self.no_stroke()
        self.background('#000000')
        self.fill('#a0a0a0')

    def draw(self):
        if self.num_iter < self.max_iter:
            [worm.draw() for worm in self.worms]
            self.num_iter += 1


if __name__ == '__main__':
    app = App(width=1200, height=800, max_iter=250)
    app.run_sketch()
