import imp
from rest_framework import serializers
from TimetableApp.models import Department, Teacher, Group, Classroom

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('DepartmentId', 'DepartmentName')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=('TeacherId', 'TeacherName', 'Department', 'Preferencies')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields=('GroupId', 'GroupNumber', 'Department')

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields=('ClassroomId', 'ClassroomNumber')
