from django.db import models

# Create your models here.
class ToDo(models.Model):
    Title = models.CharField(max_length=50, blank=False)
    Descriptions = models.TextField(blank=False)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)

    def __str__(self): 
        return self.Title
