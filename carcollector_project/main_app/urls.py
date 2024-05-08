from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Car Path
    path('cars/', views.cars_index, name='car_index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    # Rental Path
    path('cars/<int:pk>/add_rental/', views.add_rental, name='add_rental'),
    # Option Association Path
    path('cats/<int:pk>/assoc_option/<int:option_pk>', views.assoc_option, name='assoc_option'),
    path('cats/<int:pk>/assoc_delete/<int:option_pk>', views.assoc_delete, name='assoc_delete'),



    # Options Pathing
    path('options/', views.OptionList.as_view(), name='options_index'),
    path('options/<int:pk>/', views.OptionDetail.as_view(), name='options_detail'),
    path('options/create/', views.OptionCreate.as_view(), name='options_create'),
    path('options/<int:pk>/update/', views.OptionUpdate.as_view(), name='options_update'),
    path('options/<int:pk>/delete', views.OptionDelete.as_view(), name='options_delete'),

    

]