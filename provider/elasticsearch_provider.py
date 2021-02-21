from elasticsearch import Elasticsearch
from enum_class import IndexElasticEnum


def get_es():
    es = Elasticsearch(['localhost:9200'])
    print("Connect Elasticsearch")
    # es.indices.create(index=IndexElasticEnum.Food.value, body=IndexElasticMappingEnum.Food)
    return es


class ElasticsearchManager(object):
    def __init__(self, es):
        self.es = es

    def index_food(self, document):
        self.es.index(index=IndexElasticEnum.Food.value, body=document)

    def init_index(self, index_name, index_mapper_body):
        self.es.indices.create(index=index_name, body=index_mapper_body)
