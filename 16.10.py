class NonPositiveDigitException(ValueError):
    pass


class SquareException:
    def __init__(self, a):
        if a < 0:
            raise NonPositiveDigitException('Ошибка: Отрицательное значение')
        else:
            self.a = a

    def __str__(self):
        return self.a


try:
    square = SquareException(-1)
except NonPositiveDigitException as e:
    print(e)
