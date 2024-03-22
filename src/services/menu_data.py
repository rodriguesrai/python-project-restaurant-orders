import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str):
        dishes = {}
        with open(source_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])
                dish_key = f"{dish_name}_{price}"
                if dish_key not in dishes:
                    dish = Dish(dish_name, price)
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient_name), recipe_amount
                    )
                    dishes[dish_key] = dish
                else:
                    dishes[dish_key].add_ingredient_dependency(
                        Ingredient(ingredient_name), recipe_amount
                    )
        return list(dishes.values())

    def get_dishes(self):
        return self.dishes
