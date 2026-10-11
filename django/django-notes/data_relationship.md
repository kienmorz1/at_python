# Data Relationships: Users and Tasks

The task API models a relationship between users and tasks: one user can have
many tasks, while each task belongs to one user. This is a **one-to-many**
relationship.

## Defining the relationship

The relationship is represented on the `Task` model with a foreign key:

```python
class Task(models.Model):
    # Other task fields...
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks_details",
    )
```

`ForeignKey(User, ...)` stores the relationship on each task. In the database,
each task row has a `user_id` value that points to a row in the user table.
Many task rows can point to the same user, but each task row has only one
`user_id`.

`on_delete=models.CASCADE` means that deleting a user also deletes that user's
tasks. Choose a different `on_delete` behavior if tasks should be preserved
when their user is deleted.

`related_name="tasks_details"` names the reverse relationship. Given a user
instance, `user.tasks_details` accesses the related task manager, and
`user.tasks_details.all()` returns a queryset of that user's tasks. The
forward relationship works in the other direction: `task.user` returns the
task's user.

## Serializing the related data

The ordinary model serializers expose model fields:

```python
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
```

`TaskSerializer` includes the task's `user` foreign-key value. `UserSerializer`
serializes a user but does not automatically include a list of that user's
tasks.

The endpoint's response needs a custom shape containing both a user and a list
of tasks, so it uses a wrapper serializer:

```python
class AllTaskUserSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    task_list = TaskSerializer(many=True, read_only=True)
```

`user` is one object and is serialized with `UserSerializer`. `task_list` is a
collection, so `TaskSerializer` is configured with `many=True`. Both fields
are read-only because this serializer is for representing a response, not
creating or updating these objects.

The `TaskUserSerializer` with `depth = 1` is another serializer in the app. It
serializes a task with its related user nested. The user-tasks endpoint does
not use it; it uses `AllTaskUserSerializer` to put one user beside a list of
tasks.

## The user-tasks endpoint

The user viewset defines a detail action:

```python
@action(detail=True, methods=["GET"], url_path="tasks")
def get_tasks_of_a_user(self, request, pk=None):
    user = self.get_object()
    if len(user.tasks_details.all()) > 0:
        serializer = AllTaskUserSerializer({
            "user": user,
            "task_list": user.tasks_details.all(),
        })
        return Response(serializer.data)
    else:
        return Response({"error": "No Tasks Found"}, status=404)
```

`detail=True` makes the action operate on an individual user, whose primary
key is included in the URL. The router exposes it as:

```text
GET /api/users/<user-id>/tasks/
```

`self.get_object()` retrieves the user identified by `<user-id>` from the
viewset's `User.objects.all()` queryset. If the user does not exist, the
standard detail lookup returns 404. For a user with tasks, the action gets
those tasks through the reverse relationship and passes both values to
`AllTaskUserSerializer`.

The response for a user with tasks is shaped like this:

```json
{
  "user": {
    "id": 1,
    "first_name": "Ada",
    "last_name": "Lovelace",
    "email": "ada@example.com"
  },
  "task_list": [
    {
      "id": 7,
      "title": "Review the report",
      "description": "Check the latest draft",
      "completed": false,
      "user": 1
    }
  ]
}
```

As currently implemented, if the user exists but has no tasks, the action
returns `404` with `{"error": "No Tasks Found"}`. If an empty list is more
appropriate for the API, the action can instead always serialize the user and
the queryset; `task_list` will then be `[]`.
