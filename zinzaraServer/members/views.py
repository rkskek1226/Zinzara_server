from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Members
from .serializers import MembersSerializer


# Create your views here.
# Controller의 역할로 모델과 뷰를 연결하는 역할


@csrf_exempt
def members(request):
    if request.method == "POST":   # 사용자 추가하기
        data = JSONParser().parse(request)
        serializer = MembersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=210)
        return JsonResponse(serializer.errors, status=410)


@csrf_exempt
def members_info(request):
    data = JSONParser().parse(request)
    search_id = data["user_id"]
    obj = Members.objects.get(user_id=search_id)

    if data["pw"] == obj.pw:
        if request.method == "DELETE":  # 사용자 삭제하기
            obj.delete()
            return HttpResponse(status=230)

        elif request.method == "GET":  # 사용자 정보 가져오기
            serializer = MembersSerializer(obj)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == "PUT":   # 사용자 정보 수정하기
            serializer = MembersSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=220)
            return JsonResponse(serializer.errors, status=420)

    else:
        return HttpResponse(status=430)


@csrf_exempt
def login(request):   # 로그인
    if request.method == "POST":
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        obj = Members.objects.get(user_id=search_id)

        if data["pw"] == obj.pw:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

