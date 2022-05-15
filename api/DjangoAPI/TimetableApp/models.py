from django.db import models

# Create your models here.

class Department(models.Model): #Faculty - name, only Name field
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Teacher(models.Model):
    TeacherId = models.AutoField(primary_key=True)
    TeacherName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    Preferencies = models.CharField(max_length=500)

class Group(models.Model):
    GroupId = models.AutoField(primary_key=True)
    GroupNumber = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)

class Classroom(models.Model):
    ClassroomId = models.AutoField(primary_key=True)
    ClassroomNumber = models.CharField(max_length=500)


