from elasticsearch import Elasticsearch


def get_es():
    es = Elasticsearch(
        ['localhost:9200'], sniff_on_start=True,
        sniff_on_connection_fail=True,
        sniffer_timeout=60)
    print("Connect Elasticsearch")
