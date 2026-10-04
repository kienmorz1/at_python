from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from typing import override
import json

# Create your views here.
TASK_FILE_NAME="tasks_mgmt/files/task.json"
## This decorator converts add_numbers() as view

# def _get_all_tasks():
#     with open(TASK_FILE_NAME,"r") as task_file:
#         return json.loads(task_file.read())

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
    

# @api_view()
# def get_all_tasks(request):
#     output = _get_all_tasks()
#     return Response(output)

# @api_view()
# def get_tasks_by_id(request, id):
#     try:
#         output = _get_all_tasks()
#         for task in output:
#             if task["id"] == id:
#                 return Response(task)
#         return Response({"error": f"Task {id} Not Found"},status=404)
#     except:
#         return Response({"error":"Invalid Request"} ,status=400)

# @api_view(['POST'])
# def create_task(request):
#     data = request.data
#     tasks = __get_all_tasks()
#     task = {
#         "id": len(tasks) + 1,
#         "title": data["title"],
#         "description": data["description"],
#         "completed": data["status"],
#     }
#     with open(TASK_FILE_NAME, 'w') as file:
#         tasks.append(task)
#         json.dump(tasks, file, indent=4)
#     return Response({"message":"Task Created!!!"},status=201)

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