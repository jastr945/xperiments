from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl import DocType, Index, fields
from .models import Article


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
        model = Article
        fields = [
            'title',
            'body',
            'author',
            'date',
            'category',
            'source',
        ]
