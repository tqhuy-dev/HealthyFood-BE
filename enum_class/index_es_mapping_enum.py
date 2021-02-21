from enum_class import default_enum
import enum


class IndexElasticMappingEnum(enum.Enum, metaclass=default_enum.DefaultEnumMeta):
    Food = {
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
                "id": {
                    "type": "integer"  # formerly "string"
                },
                "name": {
                    "type": "text"
                },
                "price": {
                    "type": "double"
                },
                "status": {
                    "type": "integer"
                },
                "order_total": {
                    "type": "integer"
                },
                "rate": {
                    "type": "integer"
                },
                "type_food": {
                    "type": "integer"
                },
                "unit": {
                    "type": "text"
                },
                "image": {
                    "type": "text"
                }
            }
        }
    }
