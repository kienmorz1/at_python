# ViewSets

A **ViewSet** groups the API actions for one resource in one class.
For example, a task ViewSet can list, retrieve, create, update, and delete tasks.

A regular Django REST Framework (DRF) view uses HTTP methods, such as `get()`
and `post()`. A ViewSet uses actions, such as `list()` and `create()`.
A router maps request methods and URLs to these actions.

## Select a ViewSet type

Choose a ViewSet type based on the actions that the API needs:

| ViewSet type | Actions | Example use |
| --- | --- | --- |
| `ViewSet` | Only the actions that you define | A custom endpoint or a non-model operation |
| `ReadOnlyModelViewSet` | List and retrieve | A read-only product catalog |
| `ModelViewSet` | List, retrieve, create, update, partial update, and delete | A task API with standard CRUD operations |

Use `ModelViewSet` when the API needs the standard model operations.
Use `ReadOnlyModelViewSet` when clients must only read model data.
Use `ViewSet` when you need to define each action yourself.

## Create a model ViewSet

Set `queryset` to define the model records that the ViewSet can access.
Set `serializer_class` to define how DRF converts model data to and from API
data.

```python
from rest_framework.viewsets import ModelViewSet

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

`Task.objects.all()` returns all tasks. A filtered queryset returns only
matching tasks:

```python
Task.objects.filter(completed=False)
```

This query returns tasks that are not complete.

## Add a serializer

Use `ModelSerializer` to create a serializer from a Django model.
Set the model and the fields in the serializer's `Meta` class.

```python
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
```

Use an explicit list of fields if the API must expose only selected fields.

```python
fields = ["id", "title", "description", "completed"]
```

## Add routes

Use `DefaultRouter` to create the collection and detail routes.

```python
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet


router = DefaultRouter()
router.register("tasks", TaskViewSet)

urlpatterns = router.urls
```

Include these URL patterns in the project's URL configuration. For example:

```python
from django.urls import include, path

urlpatterns = [
    path("api/", include(router.urls)),
]
```

The router creates routes like these:

| Request | Action | Example URL |
| --- | --- | --- |
| `GET` | `list` | `/api/tasks/` |
| `POST` | `create` | `/api/tasks/` |
| `GET` | `retrieve` | `/api/tasks/1/` |
| `PUT` | `update` | `/api/tasks/1/` |
| `PATCH` | `partial_update` | `/api/tasks/1/` |
| `DELETE` | `destroy` | `/api/tasks/1/` |

The router gets the route name from `queryset`. If the ViewSet does not define
`queryset`, set `basename` when you register it:

```python
router.register("tasks", TaskViewSet, basename="task")
```

## Use a read-only ViewSet

Use `ReadOnlyModelViewSet` when clients can view records but cannot change
them. For example, a product catalog can support list and detail requests.

```python
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

This ViewSet provides `list()` and `retrieve()`. It does not provide create,
update, or delete actions.

## Define actions in a basic ViewSet

A basic `ViewSet` does not provide model actions automatically.
Define the actions that the API needs.
For example, this ViewSet lists tasks and retrieves one task:

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ViewSet):
    def list(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(
                {"error": "Task not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TaskSerializer(task)
        return Response(serializer.data)
```

Add other actions, such as `create()` or `destroy()`, only if the API needs
them. Use `ModelViewSet` instead when the API needs the standard CRUD actions.

## Add a custom action

Use the `@action` decorator to add an endpoint that does not match a standard
CRUD action. For example, add an endpoint that returns only completed tasks:

```python
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=["get"], url_path="completed")
    def completed(self, request):
        tasks = self.get_queryset().filter(completed=True)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
```

`detail=False` adds the action to the task collection. The router creates this
endpoint:

```text
GET /api/tasks/completed/
```

Use `detail=True` for a custom action on one task, such as an operation on
`/api/tasks/1/...`.

## Summary

- Use `ModelViewSet` for standard create, read, update, and delete operations.
- Use `ReadOnlyModelViewSet` for list and detail requests only.
- Use `ViewSet` when you need to define the actions yourself.
- Use `@action` for an additional endpoint, such as `/api/tasks/completed/`.
- Use a router to map URLs and HTTP methods to ViewSet actions.
