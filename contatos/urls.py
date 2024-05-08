from django.urls import path
from . import views

urlpatterns = [
    path('contatos/', views.ContatoListCreate.as_view(), name='contatos-list-create'),
    path('contatos/<int:pk>/', views.ContatoRetrieveUpdateDestroy.as_view(), name='contatos-detail'),
]