from django.db import models
from user.models import User

# Create your models here.
class Todo(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    priority_level = (
            ('H', 'High'),
            ('M', 'Medium'),
            ('L', 'Low')
        )
    priority = models.CharField(max_length=20, default='High', choices=priority_level)
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=False, null=False)


    def __str__(self):
        return self.title