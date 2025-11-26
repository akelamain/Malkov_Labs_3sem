from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    print("Тестирование классов геометрических фигур\n")
    
    rectangle = Rectangle(5, 5, "синий")
    circle = Circle(5, "зеленый")
    square = Square(5, "красный")
    
    print("Созданные фигуры:")
    print(f"1. {rectangle}")
    print(f"2. {circle}")
    print(f"3. {square}")

if __name__ == "__main__":
    main()