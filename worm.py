from random import random
from numpy import pi, cos, sin

from typing import Sequence

from app import App


class Worm:
    """Класс, представляющий червя Перлина и способ его визуализации.

    Attributes:
        x (float | int): Координата x текущего сегмента червя в пикселях.
        y (float | int): Координата y текущего сегмента червя в пикселях.
        radius (float | int): Радиус текущего сегмента червя в пикселях.
        length (float | int): Длина червя в пикселях.
        angle (float | int): Текущий угол взгляда червя в радианах.
        app (App): Приложения, связанное с червем.
    """
    
    def __init__(self, pos: Sequence[int | float], app: App) -> None:
        """Инициализирует объект червя Перлина
        
        Args:
            pos (Sequence[int | float]): Последовательность из двух чисел (x, y), задающих позицию.
            app (App): Экземпляр класса App, к которому принодлежит объект.
        """
        self.x, self.y = pos
        self.radius = 1
        self.length = 1.7
        self.angle = random() * pi * 2
        self.app = app

    def step_and_draw(self) -> None:
        """Делает один шаг по времени и отображает текущее состояние"""
        if self.radius > 0:
            if self.app.num_iter < self.app.max_iter:
                self.app.circle(self.x, self.y, self.radius)

                # Случайно меняем угол взгляда с помощью шума
                self.angle += self.app.noise(0.1 * (self.x + self.app.num_iter),
                                             0.1 * self.y) * 2 * pi - pi

                # Делаем шаг в направлении взгляда
                self.x += cos(self.angle) * self.length
                self.y += sin(self.angle) * self.length

                if self.app.num_iter < self.app.max_iter / 2:
                    self.radius += 0.02
                else:
                    self.radius -= 0.02

                self.radius = max(1, min(3, self.radius))
