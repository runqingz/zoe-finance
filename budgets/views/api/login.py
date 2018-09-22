from django.contrib.auth import authenticate, login
from rest_framework import views, exceptions
from rest_framework.response import Response
from rest_framework import status
import jwt, json
from django.contrib.auth import authenticate

class Login(views.APIView):


    def post(self, request):
        if not request.data:
            return Response({'error': "Please provide username/password"}, status="400")
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': "incorrect username/password"}, status="403")

        payload = {
            'id': user.id,
            'email': user.email
        }
        jwt_token = {"token": jwt.encode(payload, "finance_sercret_key").decode('utf-8')}

        return Response(
            json.dumps(jwt_token),
            status=200,
            content_type="application/json"
        )

