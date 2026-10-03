from django.urls import path
# from .views import add_numbers, get_all_tasks, get_tasks_by_id, TaskView
from .views import add_numbers, TaskView

urlpatterns = [
    # path("add-numbers/", add_numbers),
    # path("get-all-tasks/",get_all_tasks),
    # path("get-tasks-by-id/<int:id>",get_tasks_by_id),
    # path("create-task/",create_task)
    path("add-numbers/", add_numbers),
    path("tasks/",TaskView.as_view()),
    path("tasks/<int:id>/",TaskView.as_view())
]