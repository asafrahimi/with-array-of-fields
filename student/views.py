from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . import views
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.parsers import JSONParser
from .models import Id, Studentarr
from .serializers import IdSerializer, StudentarrSerializer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.models import student
def index_student(request):
    return HttpResponse("<h1>This is the student app homepage</h1>")
'''
class IdList(APIView):

    def get(self, request):
        items = Id.objects.all()
        serializer = IdSerializer(items, many =True)
        return JsonResponse(serializer.data, safe =False)
        #id = Id.objects.all()
        #serializer = IdSerializer(id, many=True)
        #return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        id_data = request.data
        new_id = Id.objects.create(name=id_data["name"], last_name=id_data["last_name"], age=id_data["age"])
        new_id.save()
        serializer = IdSerializer(new_id)
        return Response(serializer.data)

    def delete(request, nm):
        item = Id.objects.get(id = nm)
        item.delete()
        return ("item deleted")
'''

@csrf_exempt
def ItemsView(request):

    if request.method == 'GET':
        items = Id.objects.all()
        serializer = IdSerializer(items, many =True)
        #items1 = Studentarr.objects.all()
        #serializer1 = StudentarrSerializer(items1, many =True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =IdSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def ItemView(request,nm):
    try:
        item = Id.objects.get(i_d = nm)
        #item = Id.objects.filter(Id = 'student_array')
    except Id.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = IdSerializer(item)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IdSerializer(item,data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == 'DELETE':
        item.delete()
        #return render(request, 'del_done.html')
        return HttpResponse(status =204)





#class List_student(APIView):

#    authentication_classes = [authentication.TokenAuthentication]
#    permission_classes = [permissions.IsAdminUser]

#    def get(self, request, format=None):
#        students = [student.name for student in Student.objects.all()]
#        return Response(students)


#def index_student(request):
#    return HttpResponse("<h1>This is the student app homepage</h1>")
