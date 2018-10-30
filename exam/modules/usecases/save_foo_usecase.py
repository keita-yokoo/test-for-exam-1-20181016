from exam.repository.foo_repository import FooRepository
from exam.modules.entities.Foo import Foo


class SaveFooUseCase:

    def __init__(self, foo_repo: FooRepository =FooRepository()):
        self.foo_repo = foo_repo

    def execute(self, foo: Foo):
        self.foo_repo.save(foo)
