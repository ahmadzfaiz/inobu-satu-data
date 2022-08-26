from django.contrib.auth.models import User
from rest_framework import status, generics, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .serializers import ArticleSerializer, UserSerializer

#🔐USER REGISTRATION
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#📜MODEL BASED VIEWSET METHOD
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #Authentication if not default
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
