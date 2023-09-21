from rest_framework import serializers
from .models import Todo

# Serializer for the Todo model
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('ID', 'NAME', 'DATE', 'DUE', 'FEE', 'CONTACT_NO', 'EMAIL', 'STATUS')
