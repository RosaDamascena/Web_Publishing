from django.urls import path
from . import views

app_name = 'menus'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:menu_pk>/delete', views.delete, name='delete'),
]