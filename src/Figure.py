class Figure:

    def __init__(self):
        raise RuntimeError("Нельзя создавать экземпляр класса Figure")

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError("Передан объект некорректного класса.")