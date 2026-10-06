from django.urls import path
from .views import get_server_status, inspect, get_server, task_queue, legacy_server_details

app_name = "ops"

urlpatterns = [
    path("inspect/", inspect),
    path("servers/<int:server_id>/", get_server, name="server-details"),
    path("servers/status/<str:status>/", get_server_status, name="server-status"),
    path("tasks/", task_queue),
    path("node/<int:node_id>/", legacy_server_details, name="legacy-server-details"),
]