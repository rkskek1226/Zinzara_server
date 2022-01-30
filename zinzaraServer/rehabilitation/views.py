from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Language_rehabilitation, Physical_rehabilitation
from .serializers import PhysicalSerializer, LanguageSerializer
from members.models import Members


# Create your views here.


@csrf_exempt
def language_rehabilitation(request, pk):
    # if request.method == "POST":   # 언어 재활 점수 등록
    #     data = JSONParser().parse(request)
    #     serializer = LanguageSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, safe=False)
    #
    # elif request.method == "GET":   # 언어 재활 정보(점수, 시간) 가져오기
    #     pass
    data = JSONParser().parse(request)
    search_id = data["user_id"]
    obj = Members.objects.get(user_id=search_id)

    if data["pw"] == obj.pw:
        obj = Language_rehabilitation.objects.get(user_id=search_id)
        if request.method == "GET":   #언어 재활 정보(점수, 시간) 가져오기
            serializer = LanguageSerializer(obj)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == "POST":   # 언어 재활 점수 등록
            serializer = LanguageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)

    else:
        return HttpResponse(status=445)


@csrf_exempt
def physical_rehabilitation(request):
    data = JSONParser().parse(request)
    search_id = data["user_id"]
    obj = Members.objects.get(user_id=search_id)

    if data["pw"] == obj.pw:
        obj = Physical_rehabilitation.objects.get(user_id=search_id)
        if request.method == "GET":  # 언어 재활 정보(점수, 시간) 가져오기
            serializer = PhysicalSerializer(obj)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == "POST":  # 언어 재활 점수 등록
            serializer = PhysicalSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)

    else:
        return HttpResponse(status=446)
