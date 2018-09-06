from django.contrib.auth import authenticate, logout
from rest_framework import views, exceptions
from rest_framework.response import Response
from rest_framework import status

class Logout(views.APIView):


    def get(self, request):
        logout(request)
        return Response({'Success': 'successfully logged out'},
                        status=status.HTTP_200_OK)
