from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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
        tasks = self._get_all_tasks()
        task = {
            "id": len(tasks) + 1,
            "title": data["title"],
            "description": data["description"],
            "completed": data["status"],
        }
        with open(TASK_FILE_NAME, 'w') as file:
            tasks.append(task)
            json.dump(tasks, file, indent=4)
        return Response({"message":"Task Created!!!"},status=201)
    
    # @override
    # def post(self, request, url="hello-world"):
    #     return Response({"message":"Hello world"},status=201)

    @override
    def get(self,request, id=None):
        if id is None:
            output = self._get_all_tasks()
            return Response(output)
        else:
            try:
                output = self._get_all_tasks()
                for task in output:
                    if task["id"] == id:
                        return Response(task)
                return Response({"error": f"Task {id} Not Found"},status=404)
            except:
                return Response({"error":"Invalid Request"} ,status=400)

    @override
    def put(self, request, id):
        tasks = self._get_all_tasks()
        task = next((task for task in tasks if task["id"] == id), None)
        if task is None:
            return Response({"error": f"Task {id} Not Found"}, status=404)

        for field in ("title", "description", "status", "completed"):
            if field in request.data:
                task[field] = request.data[field]

        self._save_all_tasks(tasks)
        return Response(task)

    @override
    def delete(self, request, id):
        tasks = self._get_all_tasks()
        task = next((task for task in tasks if task["id"] == id), None)
        if task is None:
            return Response({"error": f"Task {id} Not Found"}, status=404)

        tasks.remove(task)
        self._save_all_tasks(tasks)
        return Response(status=204)