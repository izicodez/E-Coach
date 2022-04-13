from django.db import models

# Create your models here.
# item is athlete
class List(models.Model):
    item = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '|' + str(self.completed)