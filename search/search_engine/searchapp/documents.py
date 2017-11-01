from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from django_elasticsearch_dsl import DocType, Index, fields
from .models import Article
from elasticsearch_dsl.connections import connections


# Create a connection to ElasticSearch
connections.create_connection(hosts=['localhost:9200'], http_auth='elastic:changeme')

# Name of the Elasticsearch index
article = Index('articles')

article.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@article.doc_type
class ArticleDocument(DocType):
    class Meta:
        model = Article # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'body',
            'author',
        ]
