from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.color_obj = FigureColor(color)
    
    def calculate_area(self):
        return self.width * self.height
    
    def __repr__(self):
        return "{} цвета {} шириной {} и высотой {}. Площадь: {:.2f}".format(
            self.get_name(),
            self.color_obj.color,
            self.width,
            self.height,
            self.calculate_area()
        )