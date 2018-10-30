from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView
from exam.gateways.foo_gateway import FooGateway
from exam.modules.usecases.save_foo_usecase import SaveFooUseCase

import logging


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        # パラメータ受け取り
        print("=============================================")
        print(request.POST)
        print("=============================================")
        # param = request.GET.get("foo_value", "999999")
        foo_dict = {
            "value": "test"
        }

        # パラメータをドメインで解釈できる形に変換（dict > entity）
        foo_entity = FooGateway.dict_to_entity(foo_dict)

        # usecaseを実施する
        # use_case = SaveFooUseCase()
        # use_case.execute(foo_entity)

        context = {
            "foo": "test"
        }
        logger = logging.getLogger(__name__)
        logger.info(context)
        logger.debug("DEBUG")

        return render(request, 'index.html', context=context)

    def post(self, request, **kwargs):
        # パラメータ受け取り
        print("=============================================")
        print(request.POST)
        print("=============================================")

        context = {
            "foo": "test"
        }

        return render(request, 'index.html', context=context,)