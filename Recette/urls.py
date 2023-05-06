from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
# from .views import CustomRegisterView, profile

urlpatterns = [
    path('index/', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>', recipe_detail, name='recipe_detail'),
    path('search/', search, name="search"),
    path('accounts/profile/', profile, name='profile'), 
    path('recipe/<int:recipe_id>/rate/', rate_recipe, name='rate_recipe'),
    path('register/', register, name='register'),
    path('login/', Login_user, name='login'),
    path('logout/', Logout_user, name='logout'),
    path('recipe/<int:recipe_id>/add_comment/', add_comment, name='add_comment'),
    path('addToFavourites/<int:pk>', addToFavourites, name='addToFavourites'),
    path('removeFromFavourites/<int:pk>', removeFromFavourites, name='removeFromFavourites'),
    path('removeFromFavouritesAcceuil/<int:pk>', removeFromFavouritesAcceuil, name='removeFromFavouritesAcceuil'),

]
