# from django.conf.urls import url

# from .views import HomeTemplateView


# urlpatterns = [
#     url('', HomeTemplateView.as_view()),
# ]

from django.urls import path
from .views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view()),
]