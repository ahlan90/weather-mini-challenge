from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from weather.views import CheckTakeUmbrelaFiveDaysView

schema_view = get_schema_view(
   openapi.Info(
      title="Weather Mini Challenge - Umbrella API",
      default_version='v1',
      description="Umbrella API using Django Framework",
      contact=openapi.Contact(email="ahlan90@gmail.com")
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/umbrella', CheckTakeUmbrelaFiveDaysView.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
