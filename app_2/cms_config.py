from cms.app_base import CMSAppConfig

from djangocms_internalsearch.base import BaseSearchConfig

from .models import Model1, Model2


class TestModel1Config(BaseSearchConfig):
    model = Model1
    list_display = ['field1', 'field2']

    def prepare_text(self, obj):
        return "Lorem ipsum..."


class TestModel2Config(BaseSearchConfig):
    model = Model2
    list_display = ['field1', 'field2']

    def prepare_text(self, obj):
        return "Lorem ipsum..."


class CMSApp2Config(CMSAppConfig):
    djangocms_internalsearch_enabled = True
    internalsearch_config_list = [TestModel1Config, TestModel2Config]
