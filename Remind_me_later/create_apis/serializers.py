from rest_framework import serializers
from .models import * 

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['date', 'time', 'message']
        