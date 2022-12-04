from django.urls import path

from .views import CreateAuthorView


urlpatterns = [
    path('create-author/', CreateAuthorView.as_view(), name='create-author'),
]
