# Pagination, Filtering, Search, and Ordering

These API features let clients narrow a collection response and control how
the results are divided and sorted. In this project, they are configured on
the DRF `TaskViewSet` and `UserViewSet`, with the shared default pagination
class and filter backend in `config/settings.py`.

## Pagination

Pagination returns a collection in smaller chunks instead of returning the
entire result set in one response. The project uses DRF's
`LimitOffsetPagination`, configured in `tasks_mgmt/pagination.py`:

```python
from rest_framework.pagination import LimitOffsetPagination


class TaskPagination(LimitOffsetPagination):
    default_limit = 1
    max_page_size = 1
```

`default_limit` is the number of records returned when the request does not
provide a `limit`. `LimitOffsetPagination` uses the `limit` and `offset` query
parameters:

```text
/api/tasks/?limit=5&offset=10
```

This requests up to five results after skipping the first ten. The response
uses pagination metadata such as `count`, `next`, `previous`, and `results`.
When `limit` is omitted, this project's default is one result.

**Configuration note:** `max_page_size` is not the limit-cap attribute for
`LimitOffsetPagination`. To enforce a maximum `limit`, define `max_limit`
instead. As currently written, `max_page_size = 1` does not cap a client
request's `limit`.

The pagination class is the global DRF default, and `TaskViewSet` also
declares it explicitly. Therefore the standard list endpoints use it unless
a view overrides or disables pagination.

## Filtering

Filtering narrows results by comparing fields with query-parameter values.
The project enables `DjangoFilterBackend` globally and uses a custom
`TaskFilter` for tasks:

```python
class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    completed = django_filters.BooleanFilter()

    class Meta:
        model = Task
        fields = ["title", "description", "completed"]
```

`title` and `description` are case-insensitive substring matches.
`completed` is a boolean filter. For example:

```text
/api/tasks/?title=jailer
/api/tasks/?description=coastal
/api/tasks/?completed=false
/api/tasks/?title=part&completed=true
```

`TaskViewSet.filterset_class = TaskFilter` selects this filter definition.
The `UserViewSet` instead uses `filterset_fields = ["is_active"]` for a
simple exact field filter:

```text
/api/users/?is_active=true
```

Use `filterset_fields` for straightforward filters on model fields. Use
`filterset_class` when filter behavior needs to be declared explicitly,
including lookup types, custom filters, or validation.

## Search

DRF's `SearchFilter` provides text search for `UserViewSet`:

```python
search_fields = ["first_name", "last_name", "email"]
```

Clients pass search terms with the `search` query parameter:

```text
/api/users/?search=kamal
/api/users/?is_active=true&search=example.com
```

Search is case-insensitive by default. This search checks the listed user
fields; it is separate from the `TaskFilter` title and description filters.

## Ordering

`TaskViewSet` uses DRF's `OrderingFilter` and allows ordering by
`created_at`:

```python
ordering_fields = ["created_at"]
ordering = ["-created_at"]
```

The default `-created_at` sorts newest tasks first. Clients can select
ascending or descending order with the `ordering` parameter:

```text
/api/tasks/?ordering=created_at
/api/tasks/?ordering=-created_at
```

Only fields listed in `ordering_fields` should be exposed for client-selected
ordering. The project's current list allows `created_at`.

## Combining the features

Filtering, ordering, and pagination can be combined in one list request:

```text
/api/tasks/?completed=false&title=chapter&ordering=-created_at&limit=10&offset=0
```

The query filters tasks first, orders the matching results, then returns the
requested slice. User filtering and search can also be combined:

```text
/api/users/?is_active=true&search=kamal&limit=10&offset=0
```

## Configuration locations

| Feature | Project configuration |
| --- | --- |
| Default pagination class and filter backend | `config/settings.py` |
| `LimitOffsetPagination` settings | `tasks_mgmt/pagination.py` |
| Task field lookups | `tasks_mgmt/filters.py` |
| Task and user filters, user search, task ordering | `tasks_mgmt/views.py` |
