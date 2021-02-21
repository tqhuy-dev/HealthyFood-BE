import enum
from enum_class import default_enum


class QueueNameEnum(enum.Enum, metaclass=default_enum.DefaultEnumMeta):
    AddMaterial = "AddMaterial"
    UpdateMaterial = "UpdateMaterial"
    SyncESFoodByList = "SyncESFoodByList"
    AddFood = "AddFood"
