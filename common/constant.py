import enum_class

STATUS_FOOD_ARRAY = (enum_class.StatusFoodEnum.Available.value,
                     enum_class.StatusFoodEnum.Closed.value,
                     enum_class.StatusFoodEnum.OutStock.value,
                     enum_class.StatusFoodEnum.OutPartialStock.value)

FOOD_TYPE_ARRAY = (
    enum_class.FoodTypeEnum.FruitCake.value,
    enum_class.FoodTypeEnum.ChocolateCake.value,
    enum_class.FoodTypeEnum.ClassicCake.value
)