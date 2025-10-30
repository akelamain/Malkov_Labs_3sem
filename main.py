import sys
import math

class BiquadraticEquation:
    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.roots_list = [] 
        self.num_roots = 0     
        self.discriminant = None

    def get_coef(self, index, prompt):
        while True:
            try:
                coef_str = sys.argv[index]
            except IndexError:
                print(prompt)
                coef_str = input()
            try:
                return float(coef_str)
            except ValueError:
                print("Ошибка: коэффициент должен быть числом. Повторите ввод.")

    def get_coefs(self):
        while True:
            self.coef_A = self.get_coef(1, "Введите коэффициент A (A != 0):")
            if self.coef_A == 0:
                print("Ошибка: коэффициент A не может быть равен 0, так как уравнение перестаёт быть биквадратным.")
                if len(sys.argv) > 1:
                    sys.argv[1] = ""
            else:
                break

        self.coef_B = self.get_coef(2, "Введите коэффициент B:")
        self.coef_C = self.get_coef(3, "Введите коэффициент C:")

    def calculate_roots(self):
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C

        self.discriminant = b * b - 4 * a * c
        roots = []

        if self.discriminant < 0:
            self.roots_list = []
            self.num_roots = 0
            return

        if self.discriminant == 0:
            y = -b / (2 * a)
            if y >= 0:
                roots.extend([math.sqrt(y), -math.sqrt(y)])
        else:
            sqD = math.sqrt(self.discriminant)
            y1 = (-b + sqD) / (2 * a)
            y2 = (-b - sqD) / (2 * a)
            for y in (y1, y2):
                if y >= 0:
                    roots.extend([math.sqrt(y), -math.sqrt(y)])

        self.roots_list = roots
        self.num_roots = len(roots)

    def print_roots(self):
        print(f"Коэффициенты: A={self.coef_A}, B={self.coef_B}, C={self.coef_C}")
        print(f"Дискриминант: {self.discriminant}")

        if self.num_roots == 0:
            print("Действительных корней нет.")
        else:
            print(f"Количество действительных корней: {self.num_roots}")
            print("Корни:", ", ".join(str(r) for r in self.roots_list))


def main():
    eq = BiquadraticEquation()
    eq.get_coefs()
    eq.calculate_roots()
    eq.print_roots()

if __name__ == "__main__":
    main()