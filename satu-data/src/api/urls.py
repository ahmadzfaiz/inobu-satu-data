from django.urls import path, include
from .views import UserViewSet, ArticleViewSet #ArticleList, ArticleDetail #article_list, article_detail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    #path('articles/', ArticleList.as_view()),
    #path('articles/<int:id>/', ArticleDetail.as_view()),

    #path('articles/', article_list),
    #path('articles/<int:pk>/', article_detail),
]