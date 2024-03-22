from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish("Pizza", 20.0)
    assert dish.name == "Pizza"
    assert dish.price == 20.0
    assert dish.recipe == {}
    assert repr(dish) == "Dish('Pizza', R$20.00)"

    dish2 = Dish("Pizza", 20.0)
    assert dish == dish2

    assert hash(dish) == hash("Dish('Pizza', R$20.00)")

    ingredient = Ingredient("Tomato")
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.recipe == {ingredient: 2}

    ingredient.restrictions.add("Vegetarian")
    assert dish.get_restrictions() == {"Vegetarian"}

    assert dish.get_ingredients() == {ingredient}

    with pytest.raises(ValueError):
        Dish("Pizza", -20.0)

    with pytest.raises(KeyError):
        dish.recipe[Ingredient("Invalid Ingredient")]

    dish2 = Dish("Burger", 15.0)
    ingredient2 = Ingredient("Beef")
    ingredient2.restrictions.add("Meat")
    dish2.add_ingredient_dependency(ingredient2, 1)
    assert dish2.get_restrictions() == {"Meat"}

    assert dish2.get_ingredients() == {ingredient2}
