from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class AuthController:
    @staticmethod
    def register_user(data):
        User = get_user_model()
        username = data.get('username')
        password = data.get('password')
        if not all([username, password]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username not allowed'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, password=password)
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def login_user(data):
        User = get_user_model()
        username = data.get('username')
        password = data.get('password')
        if not all([username, password]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            if not User.objects.filter(username=username).exists():
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            user = get_user_model().objects.get(username=username)
            if user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def logout_user(user):
        user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
