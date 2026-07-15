from django.db import models


# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)

#git test
class NoteApp(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()


# model_class -> create migration file in migrations folder -> database table
# create migration file
# 

# create table
# python manage.py migrate

# python shell
# python manage.py shell

# read all data from table
# model_name.objects.all()
# select * from model_name

# add/create data
# models.object.create(title="1",description="something")


# models.object.create(title="2",description="something2")
# models.object.create(title="3",description="something3",status-"True")
