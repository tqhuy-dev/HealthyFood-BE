from enum_class import default_enum
import enum


class IndexElasticEnum(enum.Enum, metaclass=default_enum.DefaultEnumMeta):
    Food = "food"
