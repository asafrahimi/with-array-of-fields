
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
#from student.views import IdList

from django.http import HttpResponse
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from student import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('student/', include('student.urls')),
    #path('Id/', views.IdList.as_view()),
    path('Id/', include('student.urls')),
    path('Studentarr/', include('student.urls')),
    #path('StudentArray/', include('student.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
