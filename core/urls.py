from django.urls import path

from core import views

app_name = 'produtorRural'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

# produtorRural (CRUD)
    path('produtor_rural/<int:produtor_id>/', views.produtor, name='produtor'),
    path('produtor_rural/create/', views.create, name='create'),
    path('produtor_rural/<int:produtor_id>/update/', views.update, name='update'),
]