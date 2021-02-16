import enum
from enum_class import default_enum


class StatusFoodEnum(enum.IntEnum, metaclass=default_enum.DefaultEnumMeta):
    Available = 1
    Closed = 2
    OutStock = 3
    OutPartialStock = 4
