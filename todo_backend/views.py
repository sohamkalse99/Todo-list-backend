from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
# from .models import Todo
from models import Todo
# from .serializers import TodoSerializer

todo_db = {}  # This will act as our 'database'
next_id = 1

class TodoView(APIView):
    def get(self, request):
        # serializer = TodoSerializer(list(todos.values()), many=True)
        # return Response(serializer.data)
        return JsonResponse(todo_db, safe = False)
    
    def post(self, request, *args, **kwargs):
        print(request.body)
        data = json.loads(request.body)
        key = data.get('key')
        value = data.get('value')
        if key in todo_db:
            return JsonResponse({"error": "Key already exists"}, status=400)
        todo_db[key] = value
        return JsonResponse({"message": "Created successfully"}, status=201)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        key = data.get('key')
        value = data.get('value')
        if key not in todo_db:
            return JsonResponse({"error": "Key does not exist"}, status=400)
        todo_db[key] = value
        return JsonResponse({"message": "Updated successfully"}, status=200)

    def delete(self, request, *args, **kwargs):
        # data = json.loads(request.body)
        key = request.GET.get('key')
        # key = data.get('key')
        if key not in todo_db:
            return JsonResponse({"error": "Key does not exist"}, status=400)
        del todo_db[key]
        return JsonResponse({"message": "Deleted successfully"}, status=200)