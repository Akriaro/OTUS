class Figure:

    def __init__(self):
        raise RuntimeError('Создание экземпляра фигуры класса запрещено')

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Объект неподдерживаемого класса был передан в метод')
        return self.area + figure.area