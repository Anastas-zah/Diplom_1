from praktikum.bun import Bun


class TestBun:

    """ Инициализация объекта"""
    def setup_method(self):
        self.bun = Bun('Краторная булка N-200i', 1255)

    """ Тест на получение названия """
    def test_get_name(self):
        assert self.bun.get_name() == 'Краторная булка N-200i'

    """ Тест на получение цены """
    def test_get_price(self):
        assert self.bun.get_price() == 1255