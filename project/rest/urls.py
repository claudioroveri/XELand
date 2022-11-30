
#JWT:  Criação de rotas protegidas REST (parte 4)
from django.contrib import admin
from django.urls import path, include
from rest.views import  LocalViewSet, MyObtainTokenPairView,  LogoutView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework_simplejwt.tokens import RefreshToken

app_name = 'rest'

#URLS e chamda REST
router = DefaultRouter()
router.register(r'LocalREST', LocalViewSet, basename='Local')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)