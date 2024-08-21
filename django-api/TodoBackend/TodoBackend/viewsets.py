from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from TodoBackend.TodoBackend.models import Todo
from TodoBackend.TodoBackend.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [AllowAny]