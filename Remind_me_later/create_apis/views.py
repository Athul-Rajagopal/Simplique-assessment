from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import ReminderSerializer
from .models import Reminder
# Create your views here.


class ReminderCreateView(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    def create(self, request,*args, **kwargs):
        serializer = ReminderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            