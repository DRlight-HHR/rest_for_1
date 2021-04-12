from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import book, temp
from .serilizations import book_s, temp_s
from django.contrib.auth import login, logout, authenticate
from rest.main_app import home


class get_all(APIView):
    def get(self, request):
        query = book.objects.filter(name='امیرحسین')
        seriliza = book_s(query, many=True)
        return Response(seriliza.data, status=status.HTTP_200_OK)


class get_temp(APIView):
    def get(self, request):
        query = temp.objects.all()
        seri = temp_s(query, many=True)
        return Response(seri.data, status=status.HTTP_200_OK)

    '''print(request.user.is_authenticated)
        if request.user.is_authenticated is False:
            return HttpResponse('you must sing in')
        else:
            query = temp.objects.all()
            seri = temp_s(query, many=True)
            return Response(seri.data, status=status.HTTP_200_OK)'''


class update_temp(APIView):
    def put(self, request, pk):
        query = temp.objects.get(pk=pk)
        seri = temp_s(query, data=request.data)
        # print(request.data['name'])
        if seri.is_valid():
            if request.data['name'] == 'امیرحسین' and request.data['password'] == 'amir13roshan80':
                print('yesssssssssssssssssss iam update')
                seri.save()
                return Response(seri.data, status=status.HTTP_201_CREATED)
            else:
                print('noooooooooooooooooooooooooooooo')
                return Response(seri.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('noooooooooooooooooooooooooooooo')
            return Response(seri.data, status=status.HTTP_400_BAD_REQUEST)
