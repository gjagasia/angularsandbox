# Create your views here.
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from foodpledge.models import Food
from foodpledge.serializers import FoodSerializer
from rest_framework import viewsets


def home(request):
    return render(request, 'index.html')


class FoodViewSet(viewsets.ViewSet):
    serializer = FoodSerializer
    queryset = Food.objects.all()

    def list(self, request):
        queryset = Food.objects.all()
        params = request.query_params.get('t')
        if params:
            queryset = queryset.filter(food_type=params)

        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Food.objects.all()
        food = get_object_or_404(queryset, pk=pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
