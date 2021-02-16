import enum
from enum_class import default_enum


class FoodTypeEnum(enum.IntEnum, metaclass=default_enum.DefaultEnumMeta):
    FruitCake = 1
    ChocolateCake = 2
    ClassicCake = 3
