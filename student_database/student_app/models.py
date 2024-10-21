from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField(unique=True)
    course = models.CharField(max_length=100)
    join_date = models.DateField()

    def __str__(self):
        return self.name

    # URL to link to the student detail page
    def get_absolute_url(self):
        return reverse("student_detail", args=[str(self.id)])
