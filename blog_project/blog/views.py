from rest_framework import generics
from .models import Post, Comment, Category,CustomUser
from .serializers import RegisterSerializer, PostSerializer, CommentSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

#user create account
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

#user login
class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key  }, status=status.HTTP_200_OK)

#Posts create and list
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
#Comment create and list for specific post
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        self.kwargs["post_id"]
        return Comment.objects.filter(post_id=post_id)
    def perform_create(self, serializer):
        post_id = self.kwargs["post_id"]
        serializer.save(post_id=post_id)
        return super().perform_create(serializer)
    
class PostRetrieveView(generics.RetrieveAPIView):
    model = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateView(generics.UpdateAPIView):
    model = Post.objects.all()
    serializer_class = PostSerializer
class PostDelete(generics.DestroyAPIView):
    model = Post.objects.all()
    serializer_class = PostSerializer
