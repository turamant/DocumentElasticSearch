from django.urls import path
from .views import add_document

urlpatterns = [
    path('add/', add_document, name='add_document'),
]
