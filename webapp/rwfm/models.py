from django.db import models

# Create your models here.

class Object(models.Model):
    obj_id = models.TextField()
    admin = models.TextField()
    readers = models.TextField()
    writers = models.TextField()

    class Meta:
        ordering = ('obj_id',)

class Subject(models.Model):
    sub_id = models.TextField()
    admin = models.TextField()
    readers = models.TextField()
    writers = models.TextField()

    class Meta:
        ordering = ('sub_id',)

