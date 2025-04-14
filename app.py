from py5 import Sketch

from worm import Worm


class App(Sketch):
    """Класс, представляющий простое приложение на py5.
    
    Приложение создает сетку из червей, каждый из которых двигается независимо.
    Использует библиотеку py5 для рендеринга.

    Attributes:
        width (int): Ширина окна в пикселях.
        height (int): Высота окна в пикселях.
        max_iter (int): Максимальное число шагов, которое может сделать червь.
    """
    
    def __init__(self, width: int, height: int, max_iter: int) -> None:
        """Инициализирует объект приложения py5
        
        Args:
            width (int): Ширина окна в пикселях.
            height (int): Высота окна в пикселях.
            max_iter (int): Максимальное число итераций.
            
        Note:
            Черви создаются на сетке с шагом 50 пикселей по обеим осям
        """
        super().__init__()
        
        self.num_iter = 0

        self.canvas_size = width, height  # Размер окна приложения
        self.max_iter = max_iter

        # Создаем червей на решетке
        self.worms = []
        for x in range(0, width, 50):
            for y in range(0, height, 50):
                self.worms.append(Worm((x, y), self))

    def settings(self) -> None:
        """Устанавливает размер окна"""
        self.size(*self.canvas_size)

    def setup(self) -> None:
        """Устанавливает параметры py5"""
        self.rect_mode(self.CORNERS)
        self.no_stroke()
        self.background('#000000')
        self.fill('#a0a0a0')

    def draw(self) -> None:
        """Совершает один шаг по времени для каждого червя"""
        if self.num_iter < self.max_iter:
            [worm.step_and_draw() for worm in self.worms]
            self.num_iter += 1
