from exam.modules.entities.Foo import Foo
from exam.gateways.foo_gateway import FooGateway


class FooRepository:

    def save(self, foo: Foo):
        foo_model = FooGateway.entity_to_model(foo)
        foo_model.save()
