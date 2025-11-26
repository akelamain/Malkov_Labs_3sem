import math
from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor


class Circle(GeometricFigure):
    def __init__(self, radius, color):
        super().__init__()
        self.radius = radius
        self.color_obj = FigureColor(color)
    
    def calculate_area(self):
       return math.pi * self.radius ** 2
    
    def __repr__(self):
       return "{} цвета {} радиусом {}. Площадь: {:.2f}".format(
            self.get_name(),
            self.color_obj.color,
            self.radius,
            self.calculate_area()
        )