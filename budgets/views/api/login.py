from django.contrib.auth import authenticate, login
from rest_framework import views, exceptions
from rest_framework.response import Response
from rest_framework import status

class Login(views.APIView):


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'Success': 'successfully logged in'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'Fail': 'incorrect username or password'},
                            status=status.HTTP_403_FORBIDDEN )
