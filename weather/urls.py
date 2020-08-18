from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from weather.views import CustomerViewSet
#
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Oowlish Challenge - Customers API",
#       default_version='v1',
#       description="Customers API using Django Framework",
#       contact=openapi.Contact(email="ahlan90@gmail.com")
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )
#
#
# router = routers.SimpleRouter()
# router.register(r'weather', CustomerViewSet, basename='weather')
#
# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
# ]


urlpatterns = [
    # path('api/', include(router.urls)),
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]