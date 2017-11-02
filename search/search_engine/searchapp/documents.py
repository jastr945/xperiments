from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from django_elasticsearch_dsl import DocType, Index, fields
from .models import Article
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import analyzer, tokenizer


# Create a connection to ElasticSearch
connections.create_connection(hosts=['localhost:9200'], http_auth='elastic:changeme')

# Name of the Elasticsearch index
article = Index('articles')

article.settings(
    number_of_shards=1,
    number_of_replicas=0
)

# a custom analyzer
html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@article.doc_type
class ArticleDocument(DocType):

    body = fields.StringField(
        analyzer=html_strip,
        fields={'raw': fields.StringField(index='not_analyzed')}
    )

    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'date',
            'category',
            'source',
        ]