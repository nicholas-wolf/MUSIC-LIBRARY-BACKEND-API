
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import MusicLibrarySerializer
from . models import MusicLibrary

@api_view(['GET','POST'])
def music_library_table(request):
    
    
    if request.method == 'GET':
        music = MusicLibrary.objects.all()
        serializer = MusicLibrarySerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        serializer = MusicLibrarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)   


@api_view(['GET', 'PUT', 'DELETE'])
def music_library_detail(request, pk):
    music = get_object_or_404(MusicLibrary, pk=pk)
    if request.method == 'GET':
        serializer = MusicLibrarySerializer(music)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = MusicLibrarySerializer(music, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


  