from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ViewSet, ModelViewSet
from .filters import TaskFilter
from .models import Task, User
from .serializers import AllTaskUserSerializer, TaskSerializer, UserSerializer
from .pagination import TaskPagination
from typing import override
import json

# Create your views here.
TASK_FILE_NAME="tasks_mgmt/files/task.json"
## This decorator converts add_numbers() as view

@api_view()
def add_numbers(request):
    try:
        a = int(request.query_params["a"])
        b = int(request.query_params["b"])
        result = a + b
    # return Response({"message":"Hello, World!!"}) ##Creates response object
        return Response({"sum": result})
    except:
        return Response({"error":"Invalid Numbers"},status=400)


@api_view(["GET"])
def tasks_with_filter(request):
    tasks = Task.objects.all()

    title = request.query_params.get("title")
    if title:
        tasks = tasks.filter(title__icontains=title)

    completed = request.query_params.get("completed")
    if completed is not None:
        normalized_completed = completed.lower()
        if normalized_completed not in {"true", "false"}:
            return Response(
                {"error": "completed must be either 'true' or 'false'"},
                status=400,
            )
        tasks = tasks.filter(completed=normalized_completed == "true")

    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


class TaskView(APIView):
    def _get_all_tasks(self):
        with open(TASK_FILE_NAME,"r") as task_file:
            return json.loads(task_file.read())

    def _save_all_tasks(self, tasks):
        with open(TASK_FILE_NAME, "w") as task_file:
            json.dump(tasks, task_file, indent=4)

    @override # This is just convention to override the method
    def post(self, request): ## cannot change the method name
        data = request.data
        serializer = TaskSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)

    # @override
    # def post(self, request, url="hello-world"):
    #     return Response({"message":"Hello world"},status=201)
    

    def get(self,request, id=None):
        try:
            if id is None:
                task = Task.objects.all()
                serializer = TaskSerializer(task, many=True)
                serialized_data = serializer.data
                return Response(serialized_data)
                
            else:
                task = Task.objects.get(id=id)
                serializer = TaskSerializer(task)
                serialized_data = serializer.data
                return Response(serialized_data)
        except Task.DoesNotExist:
            return Response({"error": f"Task {id} Not Found"}, status=404)

    @override
    def put(self, request, id):
        try:
            data = request.data
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task, data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            serializer.save()
            return Response(serializer.data, status=200)
        except Task.DoesNotExist:
            return Response({"error": f"Task {id} Not Found"}, status=404)
    
    @override
    def patch(self, request, id):
        try:
            data = request.data
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            serializer.save()
            return Response(serializer.data, status=200)
        except Task.DoesNotExist:
            return Response({"error": f"Task {id} Not Found"}, status=404)
        
    @override
    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return Response({"message": f"Task {id} Deleted"}, status=200)
        except Task.DoesNotExist:
            return Response({"error": f"Task {id} Not Found"}, status=404)

# class TaskViewSet(ViewSet):
    

#     def list(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         try:
#             task = Task.objects.get(id=pk)
#             serializer = TaskSerializer(task)
#             return Response(serializer.data)
#         except Task.DoesNotExist:
#             return Response(
#                 {"error":"Task not found"},status=404
#             )
    
#     def create(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

#     def update(self, request, pk=None):
#         try:
#             task = Task.objects.get(id=pk)
#         except Task.DoesNotExist:
#             return Response({"error": "Task not found"}, status=404)

#         serializer = TaskSerializer(task, data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=400)
#         serializer.save()
#         return Response(serializer.data, status=200)

#     def partial_update(self, request, pk=None):
#         try:
#             task = Task.objects.get(id=pk)
#         except Task.DoesNotExist:
#             return Response({"error": "Task not found"}, status=404)

#         serializer = TaskSerializer(task, data=request.data, partial=True)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=400)
#         serializer.save()
#         return Response(serializer.data, status=200)

#     def destroy(self, request, pk=None):
#         try:
#             task = Task.objects.get(id=pk)
#         except Task.DoesNotExist:
#             return Response({"error": "Task not found"}, status=404)

#         task.delete()
#         return Response(status=204)
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ["is_active"]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["first_name", "last_name", "email"]

    @action(detail=True, methods=["GET"], url_path="tasks")
    def get_tasks_of_a_user(self,request, pk=None):
        user = self.get_object()
        if len(user.tasks_details.all()) > 0:
            serializer = AllTaskUserSerializer({
                "user": user,
                "task_list": user.tasks_details.all(),
            })
            return Response(serializer.data)
        else:
            return Response(
                {"error":"No Tasks Found"},status=404
            )
        


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TaskFilter
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    @action(detail=False, methods=["GET"],url_path="completed")
    def get_only_completed_tasks(self,request):
        tasks = Task.objects.filter(completed=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)