from rest_framework import serializers
from .models import ToDo

class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'Title', 'Descriptions', 'Date', 'Completed')
