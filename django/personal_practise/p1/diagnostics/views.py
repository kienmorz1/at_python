from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as stat
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

SERVERS = {
    101: {"hostname": "prod-web-01", "status": "healthy", "region": "asia-south1"},
    102: {"hostname": "prod-db-01", "status": "degraded", "region": "us-central1"},
    103: {"hostname": "cache-01", "status": "down", "region": "europe-west1"},
}

TASK_QUEUE = []

@api_view(['GET'])
def inspect(request):
    data = {
        "method": request.method,
        "client": request.META.get('REMOTE_ADDR'),
        "query_params_tag": request.query_params.get('tag', 'default'),
        "query_params_debug": request.query_params.get('debug', "").lower() == 'true'
    }
    return Response(data, status=stat.HTTP_200_OK)

@api_view(['GET'])
def get_server(request, server_id):
    server = SERVERS.get(server_id)
    print(f"Server ID: {server_id}, Server Data: {server}")
    if server:
        return Response(server, status=stat.HTTP_200_OK)
    else:
        return Response({"error": "Server not found"}, status=stat.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_server_status(request,status):
    if status not in ['healthy', 'degraded', 'down']:
        return Response({"error": "Invalid status"}, status=stat.HTTP_400_BAD_REQUEST)
    filtered_servers = [server for server in SERVERS.values() if server["status"] == status]
    return Response({"servers": filtered_servers}, status=stat.HTTP_200_OK)

@api_view(['POST', 'GET'])
def task_queue(request):
    if request.method == 'POST':
        id = len(TASK_QUEUE) + 1
        name = request.data.get('name')
        priority = request.data.get('priority')
        if not name or not priority or priority not in ['low', 'medium', 'high']:
            return Response({"error": "Invalid Payload"}, status=stat.HTTP_400_BAD_REQUEST)
        task = {'id': id, 'name': name, 'priority': priority}
        TASK_QUEUE.append(task)
        return Response(task, status=stat.HTTP_201_CREATED)
    elif request.method == 'GET':
        return Response({"tasks": TASK_QUEUE}, status=stat.HTTP_200_OK)

@api_view(['GET'])
def legacy_server_details(request, node_id):
    reversed_url = reverse('ops:server-details', args=[node_id])
    return redirect(reversed_url, permanent=True)