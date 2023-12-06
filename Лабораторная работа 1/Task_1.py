# TODO Написать 3 класса с документацией и аннотацией типов
class Rectangle:
    def __init__(self, width: (int, float), length: (int, float)):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param width: Ширина прямоугольника
        :param length: Длина прямоугольника

        Примеры:
        >>> rectangle = Rectangle(10, 5)
        """
        if not isinstance(width, (int, float)):
            raise TypeError('Ширина прямоугольника должна быть типа int или float')
        if width <= 0:
            raise ValueError('Ширина прямоугольника должна быть положительной')
        if not isinstance(length, (int, float)):
            raise TypeError('Длина прямоугольника должен быть типа int или float')
        if length <= 0:
            raise ValueError('Длина прямоугольника должна быть положительной')
        self.width = width
        self.length = length

    def perimeter_rectangle(self):
        """
        Функция, которая считает периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(10, 5)
        >>> rectangle.perimeter_rectangle()
        Периметр прямоугольника со сторонами 10 и 5 равен 30
        """
        print(f"Периметр прямоугольника со сторонами {self.width} и {self.length} равен {2 * (self.width + self.length)}")

    def square_rectangle(self):
        """
        Функция, которая считает площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(10, 5)
        >>> rectangle.square_rectangle()
        Площадь прямоугольника со сторонами 10 и 5 равна 50
        """
        print(f"Площадь прямоугольника со сторонами {self.width} и {self.length} равна {self.width*self.length}")


class Parallelogram:
    def __init__(self, first_side: (int, float), second_side: (int, float), sin_sharp_corner: float):
        """
        Создание и подготовка к работе объекта "Параллелограмма"

        :param first_side: Длина первой стороны треугольника
        :param second_side: Длина второй стороны треугольника
        :param sin_sharp_corner: Синус осторого угла

        Примеры:
        >>> parallelogram = Parallelogram(10, 5, 0.5)
        """
        if not isinstance(first_side, (int, float)):
            raise TypeError('Первая сторона параллелограмма должна быть типа int и float')
        if not isinstance(second_side, (int, float)):
            raise TypeError('Вторая сторона параллелограмма должна быть типа int и float')
        if not isinstance(sin_sharp_corner, (int, float)):
            raise TypeError('Острый угол должен быть типа int и float')
        if first_side <= 0:
            raise ValueError('Первая сторона параллелограмма должна быть положительной')
        if second_side <= 0:
            raise ValueError('Вторая сторона параллелограмма должна быть положительной')
        if sin_sharp_corner <= 0 or sin_sharp_corner > 1:
            raise ValueError('стрый угол должен быть от 0 до 90 градусов')
        self.first_side = first_side
        self.second_side = second_side
        self.sin_sharp_corner = sin_sharp_corner

    def perimeter_parallelogram(self):
        """
        Функция, которая считает периметр паралелограмма

        Примеры:
        >>> parallelogram = Parallelogram(10, 5, 0.5)
        >>> parallelogram.perimeter_parallelogram()
        Периметр параллелограмма со сторонами 10 и 5 равен 30
        """
        print(f"Периметр параллелограмма со сторонами {self.first_side} и {self.second_side} равен {2*(self.first_side+self.second_side)}")

    def square_parallelogram(self):
        """
        Функция, которая считает площадь параллелограмма

        Примеры:
        >>> parallelogram = Parallelogram(10, 5, 0.5)
        >>> parallelogram.square_parallelogram()
        Площадь параллелограмма со сторонами 10 и 5 и острым углом 0.5 равна 25.0
        """
        print(f"Площадь параллелограмма со сторонами {self.first_side} и {self.second_side} и острым углом {self.sin_sharp_corner} равна {self.first_side*self.second_side*self.sin_sharp_corner}")


class Rhombus:
    def __init__(self, side: (int, float), first_diagonal: (int, float), second_diagonal: (int, float)):
        """
            Создание и подготовка к работе объекта "Ромб"

            :param side: Длина стороны ромба
            :param first_diagonal: Длина первой диагонали
            :param second_diagonal: Длина второй диагонали

            Примеры:
            >>> rhombus = Rhombus(10, 5, 7)
            """
        if not isinstance(side, (int, float)):
            raise TypeError('Сторона ромба должна быть типа int или float')
        if not isinstance(first_diagonal, (int, float)):
            raise TypeError('Первая диагональ должна быть положительной')
        if not isinstance(second_diagonal, (int, float)):
            raise TypeError('Вторая диагональ должна быть положительной')
        if side <= 0:
            raise ValueError('Сторона должна быть положительной')
        if second_diagonal <= 0:
            raise ValueError('Вторая диагональ должна быть положительной')
        if first_diagonal <= 0:
            raise ValueError('Первая диагональ должна быть положительной')
        self.side = side
        self.first_diagonal = first_diagonal
        self.second_diagonal = second_diagonal

    def perimeter_rhombus(self):
        """
        Функция, которая считает периметр ромба

        Примеры:
        >>> rhombus = Rhombus(10, 5, 7)
        >>> rhombus.perimeter_rhombus()
        Периметр ромба со стороной 10 равен 40
        """
        print(f"Периметр ромба со стороной {self.side} равен {4*self.side}")

    def square_rhombus(self):
        """
        Функция, которая считает площадь ромба

        Примеры:
        >>> rhombus = Rhombus(10, 5, 7)
        >>> rhombus.square_rhombus()
        Площадь ромба с диагоналями 5 и 7 равна 35
        """
        print(f"Площадь ромба с диагоналями {self.first_diagonal} и {self.second_diagonal} равна {self.first_diagonal*self.second_diagonal}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
