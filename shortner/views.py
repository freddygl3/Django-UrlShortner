from django.shortcuts import render, redirect
from django.views import generic
from .models import Url
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import UrlSerializer
from rest_framework.response import Response
from rest_framework import status
import uuid

# Create your views here.

class Index(generic.TemplateView):
    template_name = "shortner/index.html"

""" class Create(View):
    def post(self, request, *args, **kwargs):
        
        url = request.POST.get('link')
        print(url)
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid) """

class Create(APIView):
    def post(self, request, format=None):
        uid = str(uuid.uuid4())[:5]
        request.data.update({"uuid":uid})
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UrlGo(View):
    def get(self, request, pk, *args, **kwargs):
        urlfinal = Url.objects.get(uuid=pk)
        return redirect(urlfinal.link)
        

