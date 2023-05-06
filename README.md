
# Compte Rendu du Projet

## Description :
### Le site web permettra aux utilisateurs de découvrir des recettes de cuisine, faire des commentaires et les noter également. 
## Fonctionnalitées définissant le Site :
### Modèles : Pour stocker les informations sur les recettes, les ingrédients, les commentaires et les notes.
Au niveau du code Python on utilise le framework Django pour définir un modèle de base de données pour une application de recettes. 

La classe `recipe` définit un modèle de recette qui contient des champs tels que le titre, la difficulté, l'URL, l'image et les ingrédients nécessaires. La méthode `__str__()` est définie pour renvoyer le titre de la recette.

La classe `RecipeRating` définit un modèle de note pour une recette. Elle utilise une clé étrangère pour lier une note à une recette et un utilisateur, ainsi qu'un champ de note entier compris entre 1 et 5.

La classe `User` hérite de la classe `AbstractUser` de Django et ajoute des relations de groupe et de permission pour les utilisateurs.

La classe `comment` définit un modèle de commentaire pour une recette. Elle utilise une clé étrangère pour lier un commentaire à une recette et à un utilisateur, ainsi qu'un champ de corps de texte et une date de création.

Enfin, la classe `favourites` définit un modèle de favori pour une recette. Elle utilise une clé étrangère pour lier une recette à un utilisateur.

Dans l'ensemble, ce code définit un modèle de base de données pour stocker les informations relatives aux recettes, aux notes, aux commentaires et aux favoris des utilisateurs pour une application de recettes.
### Vues : Pour afficher la page d'accueil, les pages des recettes, les pages des ingrédients, les pages des commentaires et les pages de profil.
Le code contient plusieurs fonctions :
- La fonction `profile(request)` : affiche le profil de l'utilisateur connecté avec une liste de ses recettes préférées.
- La fonction `search(request)` : permet de rechercher des recettes à partir d'un mot-clé donné.
- La fonction `get_recipe_blocks()` : cette fonction utilise la bibliothèque BeautifulSoup pour extraire des données sur les recettes à partir d'un site Web de recettes. Les données extraites sont stockées dans une base de données.
- La fonction `recipe_list(request)` : cette fonction affiche une liste de toutes les recettes présentes dans la base de données. Elle permet également de naviguer entre les différentes pages de la liste. Si un utilisateur est connecté, la fonction affiche également les recettes qu'il a marquées comme préférées.
- La fonction `recipe_detail(request, pk)` : cette fonction affiche les détails d'une recette spécifique sélectionnée par l'utilisateur. Elle affiche également la note moyenne attribuée par les utilisateurs à cette recette, ainsi que les commentaires laissés par les utilisateurs.

Le code utilise plusieurs bibliothèques et modules tels que `requests`, `beautifulsoup4` et `Paginator` de Django. Les templates html sont également inclus pour rendre le contenu de l'application.
### Templates : Pour afficher les données dans une mise en page attrayante.
#### base.html : 
Il s'agit d'une base de template HTML pour une application web qui permet de rechercher, voir et ajouter des recettes culinaires. Il inclut une barre de navigation avec un formulaire de recherche, des liens pour se connecter ou s'inscrire et un menu déroulant pour accéder au profil utilisateur et se déconnecter. Le code est écrit en utilisant le framework Bootstrap pour le style et la mise en page et utilise également du JavaScript pour rendre le formulaire de recherche interactif. Le code est bien structuré en utilisant des blocs de contenu (blocks) qui permettent d'ajouter du contenu spécifique dans chaque page de l'application.
#### login.html :
Ce code représente une page HTML de connexion qui utilise le framework CSS Bulma. Le code utilise également le tag Django `{% load static %}` pour charger des fichiers statiques (tels que les fichiers CSS et JS) depuis le répertoire `static` de l'application. La page affiche un formulaire de connexion qui contient des champs d'entrée pour le nom d'utilisateur et le mot de passe. Le formulaire est envoyé en utilisant la méthode POST, ce qui signifie que les informations de connexion sont envoyées de manière sécurisée au serveur. La page contient également deux liens, l'un pour créer un nouveau compte utilisateur (`Create account`), et l'autre pour accéder à la liste des recettes sans se connecter (`Continue without logging in`).
#### profile.html :
Ce code représente un modèle Django qui étend un modèle de base appelé 'base.html' et définit un contenu spécifique pour le bloc 'content'. Le modèle comprend des balises pour afficher le profil de l'utilisateur connecté, ses recettes préférées et la pagination de ces recettes. Il utilise également des balises conditionnelles pour gérer les cas où l'utilisateur n'a pas de recettes préférées. Le code contient également des liens qui permettent à l'utilisateur de supprimer des recettes de ses favoris ou de consulter une recette sans se connecter.
#### recipe_details.html :
Le code fourni est une page HTML qui affiche les détails d'une recette de cuisine, y compris les ingrédients, les instructions et les commentaires. Elle permet également aux utilisateurs connectés de noter la recette et affiche des recettes similaires à la fin de la page.
#### recipe_list.html :
Ce code est un template HTML utilisant le langage de template Django. Le fichier HTML étend un autre fichier de base `base.html` et utilise une série de balises et de filtres spécifiques à Django pour afficher une liste de recettes. 

Le code commence par vérifier si l'utilisateur est connecté ou non. Si l'utilisateur est connecté, la variable `lfinal` contenant les recettes de l'utilisateur avec des informations supplémentaires sur la recette est utilisée pour afficher les recettes. Sinon, la variable `recipes` contenant toutes les recettes est utilisée.

La boucle `for` est utilisée pour parcourir toutes les recettes dans la variable appropriée (`lfinal` ou `recipes`) et afficher les informations de chaque recette, y compris une image, une durée de préparation et une difficulté, ainsi qu'un lien vers la page de détails de la recette.

Enfin, le code utilise un système de pagination pour afficher les recettes sur plusieurs pages.
#### register.html :
C'est une page web écrite en HTML avec l'utilisation de la bibliothèque CSS Bulma. Il s'agit d'une page d'inscription contenant un formulaire avec des champs pour saisir le nom d'utilisateur, l'e-mail et deux champs de mot de passe pour une confirmation. Il y a également un bouton "Envoyer" pour soumettre le formulaire et un lien pour revenir à la page de connexion. Le formulaire utilise un jeton CSRF pour protéger contre les attaques de type CSRF.
### Authentification et autorisation : Pour les utilisateurs et un système d'autorisation pour les commentaires et les notes.
### Recherche : Pour les recettes et les ingrédients.
### Pagination : Pour les listes de recettes et d'ingrédients.
### Web scraping : Pour récupérer des informations sur les recettes et les ingrédients à partir d'autres sites de cuisine et les importer dans le site.
### requirements.txt :
Ce code est une liste de dépendances Python avec leurs versions. Ces dépendances sont nécessaires pour exécuter une application Django. Voici les dépendances incluses dans la liste:

- asgiref==3.6.0: un module qui fournit des utilitaires pour les applications Python qui utilisent ASGI (Asynchronous Server Gateway Interface).
- distlib==0.3.6: une bibliothèque pour la distribution Python.
- Django==4.1.7: un framework web Python utilisé pour le développement d'applications web.
- filelock==3.9.0: une bibliothèque Python qui fournit des mécanismes de verrouillage de fichiers.
- platformdirs==3.1.1: une bibliothèque Python pour la gestion des répertoires de configuration et de données spécifiques à la plate-forme.
- sqlparse==0.4.3: un analyseur de requêtes SQL pour Python.
- tzdata==2022.7: une base de données de fuseaux horaires pour Python.
- virtualenv==20.21.0: un outil pour créer des environnements d'exécution Python isolés.
### urls.py :
Ce code définit les URLs pour une application Django, en important les vues correspondantes depuis un fichier `views.py`. Les URLs incluent :

- `recipe_list`: affiche une liste de recettes
- `recipe_detail`: affiche les détails d'une recette particulière
- `search`: effectue une recherche de recettes
- `profile`: affiche le profil de l'utilisateur connecté
- `rate_recipe`: permet à un utilisateur de noter une recette
- `register`: affiche un formulaire d'inscription pour les nouveaux utilisateurs
- `login`: affiche un formulaire de connexion pour les utilisateurs existants
- `logout`: permet à un utilisateur de se déconnecter
- `add_comment`: permet à un utilisateur de laisser un commentaire sur une recette
- `addToFavourites`: permet à un utilisateur d'ajouter une recette à ses favoris
- `removeFromFavourites`: permet à un utilisateur de supprimer une recette de ses favoris
- `removeFromFavouritesAcceuil`: permet à un utilisateur de supprimer une recette de ses favoris depuis la page d'accueil. 

En outre, la configuration des médias est fournie pour permettre le stockage des fichiers média tels que les images des recettes.
## Outils de travail :
### Django – BeautifulSoup – MySQL
## Editeur de travail :
### Visual Studio Code
