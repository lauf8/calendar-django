from django.db import models
from helps.tracker import Tracker

from accounts.models import User

class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="routine")
    name = models.CharField(max_length=75)
    private = models.BooleanField(default=False)

class RoutineEvent(Tracker):
    routine_event_id = models.AutoField(primary_key=True)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE,related_name="routine_events_routine")
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField() 
    
    def __str__(self):
        return self.title
    
    