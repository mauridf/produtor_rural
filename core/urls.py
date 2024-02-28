from django.urls import path

from core import views

app_name = 'produtorRural'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

# user
#    path('user/create/', views.register, name='register'),
#    path('user/login/', views.login_view, name='login'),
#    path('user/logout/', views.logout_view, name='logout'),
#    path('user/update/', views.user_update, name='user_update'),

# produtorRural (CRUD)
    path('produtor_rural/<int:produtor_id>/', views.produtor, name='produtor'),
    path('produtor_rural/create/', views.create, name='create'),
    path('produtor_rural/<int:produtor_id>/update/', views.update, name='update'),
    path('produtor_rural/<int:produtor_id>/delete/', views.delete, name='delete'),

# tipoCultura (CRUD)
    path('tipo_cultura/<int:tipoCultura_id>/', views.tipoCultura, name='tipoCultura'),
    path('tipo_cultura/createTipoCultura/', views.createTipoCultura, name='createTipoCultura'),
    path('tipo_cultura/<int:tipoCultura_id>/update/', views.updateTipoCultura, name='updateTipoCultura'),
    path('tipo_cultura/<int:tipoCultura_id>/delete/', views.deleteTipoCultura, name='deleteTipoCultura'),
    path('tipo_cultura/indexTipoCultura/', views.indexTipoCultura, name='indexTipoCultura'),
    path('searchTipoCultura/', views.searchTipoCultura, name='search'),

# fazenda (CRUD)
    path('fazenda/<int:fazenda_id>/', views.fazenda, name='fazenda'),
    path('fazenda/createfazenda/', views.createFazenda, name='createFazenda'),
    path('fazenda/<int:fazenda_id>/update/', views.updateFazenda, name='updateFazenda'),
    path('fazenda/<int:fazenda_id>/delete/', views.deleteFazenda, name='deleteFazenda'),
    path('fazenda/indexFazenda/', views.indexFazenda, name='indexFazenda'),
    path('searchFazenda/', views.searchFazenda, name='search'),

# culturaPlantada (CRUD)
    path('cultura_plantada/<int:culturaPlantada_id>/', views.culturaPlantada, name='culturaPlantada'),
    path('cultura_plantada/createCulturaPlantada/', views.createCulturaPlantada, name='createCulturaPlantada'),
    path('cultura_plantada/<int:culturaPlantada_id>/updateCulturaPlantada/', views.updateCulturaPlantada, name='updateCulturaPlantada'),
    path('cultura_plantada/<int:culturaPlantada_id>/deleteCulturaPlantada/', views.deleteCulturaPlantada, name='deleteCulturaPlantada'),
    path('cultura_plantada/indexCulturaPlantada/', views.indexCulturaPlantada, name='indexCulturaPlantada'),
    path('searchCulturaPlantada/', views.searchCulturaPlantada, name='search'),

# dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]