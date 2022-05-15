from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TimetableApp.models import Department, Group, Teacher, Classroom
from TimetableApp.serializers import DepartmentSerializer, TeacherSerializer, GroupSerializer, ClassroomSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method=='GET':
        departments = Department.objects.all()
        departments_serializer=DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def groupApi(request, id=0):
    if request.method=='GET':
        groups = Group.objects.all()
        groups_serializer=GroupSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)
    elif request.method=='POST':
        group_data=JSONParser().parse(request)
        groups_serializer=GroupSerializer(data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        group_data=JSONParser().parse(request)
        group=Group.objects.get(GroupId=group_data['GroupId'])
        groups_serializer=GroupSerializer(group,data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        group=Group.objects.get(GroupId=id)
        group.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def teacherApi(request, id=0):
    if request.method=='GET':
        teachers = Teacher.objects.all()
        teachers_serializer=TeacherSerializer(teachers, many=True)
        return JsonResponse(teachers_serializer.data, safe=False)
    elif request.method=='POST':
        teacher_data=JSONParser().parse(request)
        teachers_serializer=TeacherSerializer(data=teacher_data)
        if teachers_serializer.is_valid():
            teachers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        teacher_data=JSONParser().parse(request)
        teacher=Teacher.objects.get(TeacherId=teacher_data['TeacherId'])
        teachers_serializer=TeacherSerializer(teacher,data=teacher_data)
        if teachers_serializer.is_valid():
            teachers_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        teacher=Teacher.objects.get(TeacherId=id)
        teacher.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def classroomApi(request, id=0):
    if request.method=='GET':
        classrooms = Classroom.objects.all()
        classrooms_serializer=ClassroomSerializer(classrooms, many=True)
        return JsonResponse(classrooms_serializer.data, safe=False)
    elif request.method=='POST':
        classroom_data=JSONParser().parse(request)
        classrooms_serializer=ClassroomSerializer(data=classroom_data)
        if classrooms_serializer.is_valid():
            classrooms_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        classroom_data=JSONParser().parse(request)
        classroom=Classroom.objects.get(ClassroomId=classroom_data['ClassroomId'])
        classrooms_serializer=ClassroomSerializer(classroom,data=classroom_data)
        if classrooms_serializer.is_valid():
            classrooms_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        classroom=Classroom.objects.get(ClassroomId=id)
        classroom.delete()
        return JsonResponse("Deleted Successfully", safe=False)


