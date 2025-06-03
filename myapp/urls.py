from django.urls import path
from .views import add_name, search_names, add_name_page, search_names_page

urlpatterns = [
    # API endpoints
    path('entry/', add_name, name='add_name'),
    path('search/', search_names, name='search_names'),
    
    # Web pages
    path('add_page/', add_name_page, name='add_name_page'),
    path('search_page/', search_names_page, name='search_names_page'),
]