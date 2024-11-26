import praktikum.ingredient_types


from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:

    """ Метод для установки необходимых объектов """
    def setup_method(self):
        self.burger = Burger()
        self.database = Database()

    """ Тест на выбор булки """
    def test_set_buns(self):
        bun = Bun('Name_bun', 100.0)
        self.burger.set_buns(bun)
        assert self.burger.bun == bun

    """ Тест добавление ингридиентов """
    def test_add_ingredients(self):
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Bun_name'
        mock_ingredient.get_price.return_value = 10.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        self.burger.add_ingredient(mock_ingredient)
        assert self.burger.ingredients[0].get_price() == 10.0
        assert self.burger.ingredients[0].get_name() == 'Bun_name'
        assert self.burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    """ Тест на удаление ингредиента """
    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        self.burger.add_ingredient(mock_ingredient)
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 0

    """ Тест на получение цены """
    def test_get_price_burger(self):
        self.burger.set_buns(self.database.available_buns()[0])
        self.burger.add_ingredient(self.database.available_ingredients()[0])
        self.burger.add_ingredient(self.database.available_ingredients()[3])
        assert self.burger.get_price() == 400.0

    """ Тест на получение чека """
    def test_get_receipt(self):
        self.burger.set_buns(self.database.available_buns()[0])
        self.burger.add_ingredient(self.database.available_ingredients()[0])
        self.burger.add_ingredient(self.database.available_ingredients()[3])
        expected_receipt = "(==== black bun ====)\n"\
                           "= sauce hot sauce =\n"\
                           "= filling cutlet =\n"\
                           "(==== black bun ====)\n\n"\
                           "Price: 400"
        assert expected_receipt == self.burger.get_receipt()