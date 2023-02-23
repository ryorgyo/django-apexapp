from django.db import models
from loginapp.models import User

# Create your models here.
class Room(models.Model):
  id = models.AutoField(primary_key=True)
    
class Room_user(models.Model):
  user_id = models.ForeignKey(User,on_delete=models.CASCADE)
  room_id = models.ForeignKey(Room,on_delete=models.CASCADE)

class Room_message(models.Model):
  user_id = models.ForeignKey(User,on_delete=models.CASCADE)
  room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
  message = models.TextField()

class Reaction(models.Model):
  to_user = models.ManyToManyField(User)
  status = models.BooleanField()