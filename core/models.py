from django.db import models


# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)


# model_class -> create migration file in migrations folder -> database table
# create migration file
# -python manage.py makemigrations

# create table
# python manage.py migrate
