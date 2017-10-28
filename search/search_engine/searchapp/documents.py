from django_elasticsearch_dsl import DocType, Index, fields
from .models import Article


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

# s = ArticleDocument.search().query("match", title="Bracing")
#
# for hit in s:
#     print(
#         "Article title: {}, author {}".format(hit.title, hit.author)
#     )
