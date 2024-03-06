from django.urls import path
from .views import * 

urlpatterns = [
    path('create-reminder/', ReminderCreateView.as_view(), name='create_reminder'),
]
