from django.urls import path
from .views import MovieCls

prop_obj = MovieCls()
urlpatterns = [
    path('base', prop_obj.base,name='base'),
    path('add_movie_page', prop_obj.add_movie_page,name='add_movie_page'),
    path('add_movie', prop_obj.add_movie,name='add_property'),
    path('update_movie_page', prop_obj.update_movie_page,name='update_movie_page'),
    path('movie_data_page', prop_obj.movie_data_page,name='movie_data_page'),
    path('update_movie', prop_obj.update_movie,name='update_movie'),
    path('delete_property', prop_obj.delete_movie,name='delete_property'),
    path('movie_profile', prop_obj.movie_profile,name='movie_profile'),

]