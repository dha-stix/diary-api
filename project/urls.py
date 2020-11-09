from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/token/', obtain_auth_token, name="obtain-token"),
    path('schema', get_schema_view(
        title="Diary API",
        description="An API that authenticate users and also users perform CRUD operations",
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs/', include_docs_urls(title="Diary API"))
]
