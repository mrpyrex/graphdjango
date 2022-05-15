import graphene
from graphene_django import DjangoObjectType
from .models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(self, info, **kwargs):
        return Todo.objects.all()

class CreateTodo(graphene.Mutation):

    todo = graphene.Field(TodoType)

    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        todo = Todo(title=title)
        todo.save()
        return CreateTodo(todo=todo)

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()