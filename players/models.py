from django.db import models

# Create your models here.
class Player(models.Model):
    player_id = models.IntegerField(default=0)
    first_name=models.TextField(default='',max_length=50)
    last_name=models.TextField(default='',max_length=100)
    position=models.TextField(default='',max_length=100)
    team=models.TextField(default='',max_length=100)
    def __str__(self):
        return f'{self.id}.{self.player_id}'
