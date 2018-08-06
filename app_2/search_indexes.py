from haystack import indexes
from .models import (
    Model1,
    Model2,
)


class Model1Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    achar = indexes.CharField(model_attr='fchar')
    adate = indexes.DateTimeField(model_attr='fdatetime')
    abool = indexes.BooleanField(model_attr='fbool')
    aint = indexes.IntegerField(model_attr='fint')

    def get_model(self):
        return Model1

    def prepare_text(self, obj):
        t = '{}\n{}'.format(obj.fchar, obj.furl)
        return t


class Model2Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    achar = indexes.CharField(model_attr='f2char')
    adate = indexes.DateTimeField(model_attr='f2datetime')
    abool = indexes.BooleanField(model_attr='f2bool')
    aint = indexes.IntegerField(model_attr='f2int')

    def get_model(self):
        return Model2

    def prepare_text(self, obj):
        t = '{}\n{}'.format(obj.f2char, obj.f2url)
        return t


