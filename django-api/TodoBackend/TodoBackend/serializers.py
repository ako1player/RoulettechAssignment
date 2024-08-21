from rest_framework import serializers
from TodoBackend.TodoBackend.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['name', 'created', 'updated', 'id']
        read_only_fields = ['created', 'updated', 'id']