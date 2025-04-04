from rest_framework import generics
from .serializers import UserProfileSerializer, RegisterSerializer, LoginSerializer, UpdateProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

#user profile view
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    #permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

#user create account
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    
"""#user Logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try: 
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status = 204)
        except Exception as e:
            print("Error During Logout:", str(e))
            return Response({"detail": str(e)}, status = 400)"""

class DeleteUserView(generics.DestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status = 204)

class UpdateProfileView(generics.UpdateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = UpdateProfileSerializer
    def get_object(self):
        return self.request.user