from django.contrib.auth.views import LogoutView
from contato.views import CustomLoginView
from django.urls import path
from contato import views

urlpatterns = [
    
    path("", views.landing, name="landing"),

    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
    path('painel/', views.painel, name='painel'),
    path("mensagem/<int:id>/excluir/", views.excluir_mensagem, name="mensagem_excluir"),
]
