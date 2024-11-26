import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    """ Тест на получение цен ингредиентов """
    def test_get_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_price() == 88

    """ Тест на получение названия ингредиентов """
    def test_get_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_name() == 'Соус с шипами Антарианского плоскоходца'

    """ Тест на получение типа ингридиента """
    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Плоды Фалленианского дерева', 874, 'FILLING']
        ]
    )
    def test_get_type_correct_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient