from haystack import indexes
from .models import NewsModel

class NewsModelIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return NewsModel

    def index_queryset(self, using=None):
        return self.get_model().objects.all()