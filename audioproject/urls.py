from django.db.models.expressions import F
from django.urls import path, re_path as url, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from audio import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()


router.register("songs",views.SongViewSet)
router.register("podcast",views.PodcastViewSet)
router.register("audio",views.AudiobookViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Audio Podcast Songs API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls


api_urls = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
]

urlpatterns += api_urls + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

