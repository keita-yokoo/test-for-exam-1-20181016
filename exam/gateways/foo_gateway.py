from exam.modules.entities.Foo import Foo
from exam.models.fooorm import FooORM


# Entity単位でクラス分けする
class FooGateway:

    @staticmethod
    def dict_to_entity(foo: dict):
        foo_entity = Foo(foo["value"])
        return foo_entity

    @staticmethod
    def entity_to_model(foo: Foo):
        value = foo.value
        print(value)
        foo_model = FooORM()
        foo_model.value = value
        return foo_model
