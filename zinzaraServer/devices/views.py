from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Devices
from .serializers import DevicesSerializer
from members.models import Members

# Create your views here.


@csrf_exempt
def devices(request):   # 기기 명령하기
    if request.method == "POST":
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        obj = Members.objects.get(user_id=search_id)

        if data["pw"] == obj.pw:
            serializer = DevicesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=202)
            else:
                return JsonResponse(serializer.errors, status=402)
        else:
            return HttpResponse(status=444)


@csrf_exempt
def devices_info(request):   # 기기 정보(이름, 명령어, 시간) 가져오기 및 기기 삭제하기
    data = JSONParser().parse(request)
    search_id = data["user_id"]
    obj = Devices.objects.filter(user_id=search_id)

    if request.method == "GET":
        serializer = DevicesSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "DELETE":
        obj.delete()
        return HttpResponse(status=444)
