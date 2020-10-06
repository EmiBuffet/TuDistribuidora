from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def home(request):
    return render(request, 'home.html', {'meta_title': 'Home'})


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hola, Somos Tu Distribuidora!'}
        return Response(content)