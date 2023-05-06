from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _
from django.utils import timezone

class recipe(models.Model):
    title = models.CharField(max_length=200)
    difficulty = models.TextField()
    dish = models.TextField()
    url = models.TextField()
    image = models.TextField()
    category = models.TextField()
    ingredients = models.TextField(default='no ingredients found')
    Steps = models.TextField(default='no Steps found')
    intro = models.TextField(default='no intro found')

    def __str__(self):
        return self.title
    
  
        
class RecipeRating(models.Model):
    recipe = models.ForeignKey('recipe', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey('User',  on_delete=models.CASCADE, default='')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='recette_users' 
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='recette_users_permissions'
    )

class comment(models.Model):
    recipe = models.ForeignKey(recipe, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class favourites(models.Model):
    recipe = models.ForeignKey(recipe, on_delete=models.CASCADE)
    ReqUser = models.ForeignKey(User, on_delete=models.CASCADE)
