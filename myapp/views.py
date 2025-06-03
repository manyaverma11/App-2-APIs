from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Education, Name
from .serializers import NameSerializer

def add_name_page(request):
    degrees = Education.objects.all()
    return render(request, 'add_name.html', {'degrees': degrees})

def search_names_page(request):
    return render(request, 'search_names.html')

@api_view(['POST'])
def add_name(request):
    serializer = NameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def search_names(request):
    query = request.GET.get('q', '')
    results = Name.objects.filter(first_name__icontains=query) | Name.objects.filter(last_name__icontains=query)
    serializer = NameSerializer(results, many=True)
    return Response(serializer.data)