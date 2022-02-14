from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def getRouters(request):

    return Response('Hello')


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product)

    return Response(serializer.data)
