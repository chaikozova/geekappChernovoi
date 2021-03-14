import shortuuid as shortuuid
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.tasks import send_async_email
from user.models import Users
from user.permissions import IsAdmin
from user.serializers import LoginSerializer, UserListSerializer, UserRetrieveUpdateDeleteSerializer


class LoginView(APIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id, 'email': user.email,
                         'username': user.username,
                         'first_name': user.first_name,
                         'last_name': user.last_name,
                         'is_staff': user.is_staff,
                         'token': token.key}, status=status.HTTP_200_OK)


class LogoutView(APIView):

    permission_classes = (IsAuthenticated)

    def get(self, request):
        try:
            request.user.auth_token.delete()
        except(AttributeError, ObjectDoesNotExist):
            pass

        return Response({'success': "Successfully logged out."}, status=status.HTTP_200_OK)


class UserRetrieveUpdateDeleteAPIView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserRetrieveUpdateDeleteSerializer


class UserListView(APIView):
    permission_classes = (IsAdmin)

    def get(self, request):
        queryset = Users.objects.all()
        serializer=UserListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
# @permission_classes([IsAdmin])
def reset_user_password(request):
    """
    Changing user password to something strange
    """
    user_id = request.data.get("user_id")
    if not user_id:
        return Response({"error": "Need users id to reset his password"}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(Users, pk=user_id)
    password = str(shortuuid.uuid())[:8]
    subject = "Новый пароль от вашего аккаунта."
    message = f'Hello, {user.first_name} {user.last_name}. Ваш новый пароль - "{password}"(без ковычек) . ' \
              f'Пожалуйста, не передавайте это сообщение кому либо другому.'

    email_from = settings.EMAIL_HOST_USER
    send_async_email.delay(subject, message, email_from, user.email)
    user.set_password(password)
    user.save()
    return Response({"message": "successfully updated user password"}, status=status.HTTP_200_OK)
