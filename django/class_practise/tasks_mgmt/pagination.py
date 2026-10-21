from rest_framework.pagination import LimitOffsetPagination


class TaskPagination(LimitOffsetPagination):
    default_limit = 1
    max_page_size = 1
