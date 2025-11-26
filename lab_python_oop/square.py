from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_length, color):
        super().__init__(side_length, side_length, color)
    
    def __repr__(self):
        return "{} цвета {} со стороной {}. Площадь: {:.2f}".format(
            self.get_name(),
            self.color_obj.color,
            self.width,
            self.calculate_area()
        )