from src.models.ingredient import (
    Ingredient,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():

    ingredient = Ingredient("farinha")
    assert ingredient.name == "farinha"

    ingredient = Ingredient("tomate")
    assert ingredient.name == "tomate"
    assert ingredient.restrictions == set()

    assert (
        repr(Ingredient("queijo mussarela"))
        == "Ingredient('queijo mussarela')"
    )

    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("bacon")
    assert ingredient1 == ingredient2

    ingredient1 = Ingredient("caldo de carne")
    ingredient2 = Ingredient("caldo de carne")
    assert hash(ingredient1) == hash(ingredient2)

    ingredient3 = Ingredient("cebola")
    ingredient4 = Ingredient("cenoura")
    assert hash(ingredient3) != hash(ingredient4)
