from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import View
from .serializers import ViewSerializer


# Create your views here.
@csrf_exempt
def add_info(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ViewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def update_data(request,id):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        get_info = View.objects.get(id=id)
        serializer = ViewSerializer(get_info, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def retrive_data(request, id):
    try:
        get_info = View.objects.get(id=id)
    except View.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ViewSerializer(get_info)
        return JsonResponse(serializer.data)


@csrf_exempt
def delete_data(request,id):
    try:
        if request.method == 'DELETE':
            get_info = View.objects.get(id=id)
            get_info.delete()
            return HttpResponse(status=204)
    except View.DoesNotExist:
        return HttpResponse("404",status=404)

