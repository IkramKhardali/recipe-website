from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import *
from .forms import *
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.db.models.functions import Random
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def profile(request):
    user = request.user
    us = User.objects.get(username = request.user)
    fav = favourites.objects.filter(ReqUser=us)
    return render(request, 'profile.html',{'f': fav, 'user': user})

def search(request):
    query= request.GET.get('keyword')
    recipes = recipe.objects.filter(title__contains = query)
    return render(request, 'recipe_list.html',{'recipes':recipes})

def get_recipe_blocks():
    for i in range(1, 30):
        rec = recipe()
        url = 'https://www.jamieoliver.com/recipes/category/course/mains/?rec-page='+ str(i)
        response = requests.get(url)
        html_content = response.content
        
        soup = BeautifulSoup(html_content, 'html.parser')

        recipe_blocks = soup.find_all( class_="col-lg-4 col-md-6 col-xs-6 col-sm-6 recipe-col item active")
        
        for block in recipe_blocks:
            rec = recipe()
            link = block.find('a')['href']
            parts = link.split("/")
            category = parts[2]
            dish = parts[3].replace(" ", "-")

            img_src = block.find('img')['src']

            difficulty = block.find('span', class_='difficulty').text.strip()

            title = block.find('div', class_='recipe-title').text.strip()
            rec = recipe()
            rec.title = title
            rec.image = img_src
            rec.difficulty = difficulty
            rec.dish = dish
            rec.category = category

            url = 'https://www.jamieoliver.com/recipes/'+rec.category +'/'+rec.dish+'/'
            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            try:
                intro = soup.find('div', class_='recipe-intro').text.strip()
                rec.intro = intro
            except:
                rec.intro = "Get ready to tantalize your taste buds with this amazing recipe! Whether you're an experienced cook or just starting out, this dish is sure to impress. With its flavorful blend of ingredients and easy-to-follow steps, you'll be on your way to creating a delicious meal in no time. Whether you're cooking for yourself or for a crowd, this recipe is perfect for any occasion. So roll up your sleeves, get your ingredients ready, and let's get cooking! We hope you enjoy making and eating this dish as much as we do"

            ul = soup.find('ul', {'class': 'ingred-list'})
            children = ul.findChildren("li" , recursive=False)
            liste = []
            for child in children:
                liste.append(child.text.strip())
            ingred = ";".join(liste)
            rec.ingredients = ingred

            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            ol = soup.find('ol', {'class': 'recipeSteps'})
            try:
                Ingredsteps = ol.findChildren("li" , recursive=True)
                s = []
                for li in Ingredsteps:
                    s.append(li.text.strip())
                steps = ";".join(s)
                rec.Steps = steps
                rating = RecipeRating()
                rating.recipe = rec
                rating.rating = 0

                rec.save()
                rating.save()
            except:
                print()


def recipe_list(request):


    #remove this comment to scrape data and store it in the database
    # get_recipe_blocks()
    recipes = recipe.objects.all()
    paginator = Paginator(recipes, 12)
    p = request.GET.get("page",1)
    try:
        RecipesPage = paginator.page(p)
    except PageNotAnInteger:
        RecipesPage = paginator.page(1)
    except EmptyPage:
        RecipesPage = paginator.page(1)
    
    if request.user.is_authenticated:
        us = User.objects.get(username = request.user)
        liste=[]
        for r in RecipesPage:
            isFav = favourites.objects.filter(recipe = r , ReqUser_id=us.id).exists()
            finalRec = {}
            finalRec[r.id] = isFav
            liste.append(isFav)
            lfinal = zip(RecipesPage, liste)
        return render(request, 'recipe_list.html', {'recipes':RecipesPage, 'page':p, 'isFav':liste,'lfinal':lfinal})
    return render(request, 'recipe_list.html', {'recipes':RecipesPage, 'page':p})


def recipe_detail(request, pk):
    rec = get_object_or_404(recipe, pk=pk)
    rec = recipe.objects.get(pk=pk)
    ingredients_list = rec.ingredients.split(";")
    Instructions_list = rec.Steps.split(";")
    ratings = RecipeRating.objects.filter(recipe=rec)
    avg_rating = ratings.aggregate(models.Avg('rating'))['rating__avg']
    R = {
        'recipe': recipe,
        'ratings': ratings,
        'avg_rating': avg_rating,
    }
    if request.user.is_authenticated:
        us = User.objects.get(username = request.user)
        exists = RecipeRating.objects.filter(recipe_id=pk, user_id=us.id).exists()
        comments = comment.objects.filter(recipe_id=pk)
        similar = recipe.objects.filter(category=rec.category).annotate(random_number=Random()).order_by('random_number')[:4]
        return render(request, 'recipe_details.html', {'recipe': rec, 'ingredients_list': ingredients_list, 'Instructions_list':Instructions_list, 'rating':R, 'exists':exists, 'similar':similar,'comments':comments})
    comments = comment.objects.filter(recipe_id=pk)
    similar = recipe.objects.filter(category=rec.category).annotate(random_number=Random()).order_by('random_number')[:4]
    return render(request, 'recipe_details.html', {'recipe': rec, 'ingredients_list': ingredients_list, 'Instructions_list':Instructions_list, 'rating':R,'comments':comments, 'similar':similar,})

def rate_recipe(request, recipe_id):
    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        recipe_instance = recipe.objects.get(id=recipe_id)
        my_p = User.objects.get(username = request.user)
        rating_instance = RecipeRating.objects.create(recipe=recipe_instance, user=my_p, rating=rating_value)
        rating_instance.save()
        messages.success(request, 'You have rated this recipe.')
        return redirect('recipe_detail', pk=recipe_id)
    else:
        return redirect('recipe_detail', pk=recipe_id)

def index(request):
    return render(request, 'recipe_list.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
            )
            form.save()
            user.save()
            return redirect('login')

    return render(request, 'register.html', {'form': form})


def Login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('recipe_list')
    return render(request, 'login.html')

def Logout_user(request):
    logout(request)
    return redirect('login')

def add_comment(request, recipe_id):
    rec = recipe.objects.get(id=recipe_id)

    us = User.objects.get(username = request.user)
    content = request.POST.get('content')
    if content:
        cmt = comment.objects.create(owner=us, recipe=rec, body=content)
    return redirect('recipe_detail', rec.id)

def add_to_favorites(request):
    if request.method == 'POST' and request.is_ajax():
        recipe_id = request.POST.get('recipe_id')
        rec = recipe.objects.get(pk=recipe_id)
        us = User.objects.get(username = request.user)
        us.favorite_recipes.add(rec)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def addToFavourites(request, pk):
    rec = get_object_or_404(recipe, pk = pk)
    us = User.objects.get(username = request.user)
    fav = favourites()
    fav.recipe = rec
    fav.ReqUser = us
    print(fav)
    fav.save()
    return redirect('recipe_list')   

def removeFromFavourites(request, pk):
    fav = get_object_or_404(favourites, pk = pk)
    fav.delete()
    return redirect('profile')   

def removeFromFavouritesAcceuil(request, pk):
    rec = get_object_or_404(recipe, pk = pk)
    us = User.objects.get(username = request.user)
    fav = get_object_or_404(favourites, recipe = rec, ReqUser = us)
    fav.delete()
    return redirect('recipe_list')   

