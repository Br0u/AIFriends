from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ....models.user import UserProfile


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get("username").strip()
            password = request.data.get("password").strip()
            if not username or not password:
                return Response({"error": "username or password is required"}, status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if user: #用户名存在
                user_profile = UserProfile.objects.get(username=username)
                refresh = RefreshToken.for_user(user) #生成jwt
                response = Response({
                    'result' : 'success',
                    'access' : str(refresh.access_token),
                    'user_id' : user.id,
                    'username' : user.username,
                    'photo' : user_profile.photo.url,
                    'profile' : user_profile.profile,
                })
                response.set_cookie(
                    key = 'refresh_token',
                    value = str(refresh),
                    httponly = True,
                    samesite = 'Lax',
                    secure = True,
                    max_age = 86400 * 7,
                )
                return response
            return Response({
                'result' : 'fail',
            })
        except:
            return Response({
                'result': '系统异常，稍后再试',
            })
