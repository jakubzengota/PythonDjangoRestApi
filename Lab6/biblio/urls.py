from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import  KsiazkaList
from .views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', KsiazkaList, basename='Ksiazki')
urlpatterns = router.urls