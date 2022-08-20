''' API URLS '''
from django.urls import path, include
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

Schema = get_schema_view(
   openapi.Info(
      title="API для сервиса",
      default_version='v1',
      contact=openapi.Contact(email="ruslan.gzn@gmail.com"),
   ),
   public=True,
)

urlpatterns = [
    path('login/',views.obtain_auth_token),
    path('', Schema.with_ui('redoc',), name='docs')
]