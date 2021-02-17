from enum_class import DefaultEnumMeta
import enum


class StatusMaterialTypeEnum(enum.IntEnum, metaclass=DefaultEnumMeta):
    Available = 1
    OutPartialStock = 2
    OutStock = 3
    Closed = 4
