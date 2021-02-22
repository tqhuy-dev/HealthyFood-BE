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

    def index_document(self, index_name, document):
        self.es.index(index=index_name, body=document)

    def init_index(self, index_name, index_mapper_body):
        self.es.indices.create(index=index_name, body=index_mapper_body)

    def search_index(self, index_name, query):
        result = self.es.search(index=index_name, body=query)
        print(result)
