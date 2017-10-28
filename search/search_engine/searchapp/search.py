from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()

class ArticleIndex(DocType):
    title = Text()
    body = Text()
    date = Date()
    author = Text()
    source = Text()

    class Meta:
        index = 'article-index'



client = Elasticsearch()

s = Search().using(client).query("match", title="cannon beach")

for hit in s:
    print(hit.title)
