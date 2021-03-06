from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)