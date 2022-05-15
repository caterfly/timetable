from django.urls import re_path as url
from TimetableApp import views


urlpatterns=[
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),

    url(r'^teacher$', views.teacherApi),
    url(r'^teacher/([0-9]+)$', views.teacherApi),

    url(r'^group$', views.groupApi),
    url(r'^group/([0-9]+)$', views.groupApi),

    url(r'^classroom$', views.classroomApi),
    url(r'^classroom/([0-9]+)$', views.classroomApi)
]