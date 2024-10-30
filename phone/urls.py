from django.urls import path
from . import views

urlpatterns = [
    path('add-phone/', views.add_phone, name='add_phone'),
    path('success/', views.success, name='success'),
    path('search/results/', views.phone_search_results, name='phone_search_results'),
    path('search/results2/', views.phone_search_results2, name='phone_search_results'),
    path('search/', views.search, name='search'),
    path('advanced-search/', views.advanced_search, name='search_phones'),
]
