
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Railway Management API - ASDL",
        default_version='V2.0',
        description="Railway Management API Backend Service",
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

from django.contrib import admin
from django.urls import path, include
from users.views import UserRegister, UserLogin

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path("redoc", schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),
    path('docs/', include_docs_urls(title='Finish Factory Backend'),
         name="Documentation"),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('booking/', include('booking.urls'))
]


