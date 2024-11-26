from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:

    """ Метод для инициализации объекта Database """
    def setup_method(self):
        self.database = Database()

    """ Тест на получение доступных булок """
    def test_get_available_buns(self):
        available_buns = self.database.available_buns()
        assert len(available_buns) == 3

    """ Тест на получение доступных ингридиентов """
    def test_get_available_ingredients(self):
        available_ingredients = self.database.available_ingredients()
        assert len(available_ingredients) == 6

    """ Тест на получение доступных соусов """
    def test_get_available_sauces(self):
        ingredients = self.database.available_ingredients()
        type_sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(type_sauces) == 3

    """ Тест на получение доступных начинок """
    def test_get_available_fillings(self):
        ingredients = self.database.available_ingredients()
        type_fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(type_fillings) == 3

    """ Тест на получение цен ингредиентов """
    def test_get_ingredients_price(self):
        ingredients = self.database.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}
        assert price['hot sauce'] == 100
