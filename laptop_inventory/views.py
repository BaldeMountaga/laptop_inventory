from django.http import JsonResponse
from .models import Laptop
from .serializers import LaptopSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET']) 
def laptop_list(request, format=None):
    laptops = Laptop.objects.all()
    serializers = LaptopSerializer(laptops, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def addLaptop(request, format=None):
    if request.method == 'POST':
        serializers = LaptopSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def sold_laptops(request, format=None):
    laptops = Laptop.objects.filter(sold='Yes')
    total = 0
    for laptop in laptops:
        total += laptop.price
        serializers = LaptopSerializer(laptops, many=True)
        return JsonResponse(serializers.data, safe=False)
    return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def laptop_detail(request, id, format=None):
    try:
        laptop = Laptop.objects.get(pk=id)
    except Laptop.DoesNotExist:
        return Response({'message': 'The laptop does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = LaptopSerializer(laptop)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = LaptopSerializer(laptop, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        laptop.delete()
        return Response({'message': 'Laptop was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

