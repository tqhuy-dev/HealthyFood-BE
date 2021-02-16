import enum


class DefaultEnumMeta(enum.EnumMeta):
    default = object()

    def __call__(cls, value=default, *args, **kwargs):
        if value is DefaultEnumMeta.default:
            # Assume the first enum is default
            return next(iter(cls))
        return super().__call__(value, *args, **kwargs)

        # return super(DefaultEnumMeta, cls).__call__(value, *args, **kwargs) # PY2


class StatusFoodEnum(enum.IntEnum, metaclass=DefaultEnumMeta):
    Available = 1
    Closed = 2
