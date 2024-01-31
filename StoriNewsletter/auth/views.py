from rest_framework.views import APIView

from auth.auth_controller import AuthController


class RegisterView(APIView):
    @staticmethod
    def post(request):
        return AuthController.register_user(data=request.data)


class LoginView(APIView):
    @staticmethod
    def post(request):
        return AuthController.login_user(data=request.data)


class LogoutView(APIView):
    @staticmethod
    def post(request):
        return AuthController.logout_user(user=request.user)
