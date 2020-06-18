""" Django/ Python Project """

""" SECTION 1 """
# In terminal
# 'mkdir' project folder
# cd into project folder

# setup virtual environment
# 'pip3 install virtualenv'
# 'virtualenv .env -p python3'

# 'ls -a'
# should be able to see .env in project folder

# ANCHOR activate virtual environment
# 'source .env/bin/activate'
# type 'deactivate' to exit

# now install dependencies - Django and psycopg2, continue in terminal
# 'pip3 install django'
# next, start project server on desired project folder, include . at the end with a space after your project folder
# 'django-admin startproject catcollector_project .'
# open code, check if catcollector_project is in code, no more than one folder
# if you use 'code .' then this will still work in virtual environment, you do not have to deactivate

# should remain in virtual env (.env on terminal)
# test server
# 'python3 manage.py runserver'
# next, test on given localhost:8000, rocketship should appear
# 'ctrl + c' to exit server

# 'pip3 install psycopg2'
# terminal should read "Successfully installed..."
# if install does not work, try below
# 'pip3 install psycopg2-binary'


# setup/install dependencies
# 'pip3 freeze > requirements.txt'
# if you download and run a project, install dependencies
# 'pip3 install -r requirements.txt'

# create database, make sure postgres is running
# if not, ANCHOR here are CLI for postgresql
# start - 'brew services start postgresql for mac'
# stop - 'brew services stop postgresql'
# restart - 'brew services restart postgresql'
# 'createdb catcollector'
# to verify created db, run 'psql postgres' to open postgres, then '\l' to list databases, catcollector should be listed, '\q' to exit

# in catcollector_project/settings.py, change DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catcollector',
    }
}
# make sure the NAME field matches the db name used when you created the db (line 48)

# NOTE never touch .env folder, this is similar to node_modules and should never be edited, not even the .gitignore file


# add .gitignore, use https://www.toptal.com/developers/gitignore for reference

# git add and commit





""" SECTION 2 """
# create app
# in terminal, should still be in virtual environment (ref lines 15-17)
# 'python3 manage.py startapp main_app'
# now main_app folder should appear in your code next to catcollector_project
# in catcollector_project/settings.py
# include main_app in INSTALLED_APPS like so

INSTALLED_APPS = [
	'main_app',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

# test main_app, run server 'python3 manage.py runserver'
# everything should be the same as it was
# stop server 'ctrl + c'


# migrate 
# in terminal
# 'python3 manage.py migrate'
# should see all of the OK, OK, OK...
# connect to catcollector db
# 'psql catcollector'
# '\dt' should show all tables created from migration (auth_group, auth_group_permissions, auth_permission...)
# '\q' to exit
# 'python3 manage.py runserver', errors should be gone now
# stop server 'ctrl + c'

# if you check your text editor, you should now see models.py and views.py in main_app folder

# git add and commit





""" SECTION 3 """
# in main_app folder create urls.py

# in catcollector_project/urls.py
# Add the include function to the end of import path, not admin
from django.urls import path, include

# in urlpatterns, add a root route like so
urlpatterns = [
    path('admin/', admin.site.urls),
    # In this case '' represents the root route
    path('', include('main_app.urls')),
]
# you can add the comma at the end, should not matter

# in main_app/urls.py import paths and views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
# the above route defines a root path


# in main_app/views.py
# before this line - Create your views here.
from django.http import HttpResponse

# define the home view
def home(request):
    return HttpResponse('<h1>Hello</h1>')
# HttpResponse is like res.send()

# in terminal, start server
# 'python3 manage.py runserver'
# page with rocketship should be replaced with 'Hello'


# to add any new paths, or to set final render paths
# in main_app create templates folder
# in main_app/templates create about.html
# setup boilerplate html with <h1>About</h1> for testing
# in main_app/urls.py add path to urlpatterns
    path('about/', views.about, name='about')
# NOTE make sure all previous paths have a comma afterwards

# in main_app/views.py
# create about function
# instead of HttpResonse, render file
def about(request):
    return render(request, 'about.html')
# add render to final viewing instead of HttpResponse
# this will now render a file with styles

# test, run server
# 'python3 manage.py runserver'
# view page at localhost:8000/about/

# return to home route and change home function to
def home(request):
    return render(request, 'home.html')
# in main_app/templates create home.html
# setup boiler plate with <h1>Home</h1> for testing

# when server is running, you should see all paths working with an h1 tag as content
# NOTE reminder, when running server, make sure you are in the virtual environment, make sure it is active (reference lines 15-17)

# stop server, 'ctrl + c'
# git add and commit
# NOTE you can stay in virtual environment to add and commit





""" SECTION 4 """
# for layouts/partials
# in main_app/templates create base.html
# setup content that exists across all pages
# in header, add links to all pages so moving between routes is easier
<a href="/">Home</a>
<a href="/about">About</a>
# in main section, set tags for reference
{% block content %}
{% endblock %}

# in main_app/templates/about.html and home.html
# remove all content
# add extending tag at the top
{% extends 'base.html' %}
# wrap content in following tags
{% block content %}
    # content goes here
{% endblock %}


# in main_app create static folder(same as public)
# in main_app/static create css/styles.css
# link css to base.html
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
# you can also include this link for testing or using materialize, probably shouldn't add it though
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
# load static
# at top of base.html before !DOCTYPE
{% load static %}
# restart server, 'ctrl + c' to stop, 'python3 manage.py runserver' to start


# creating nested views, if you want to test content
# in main_app/views.py
# add class & list under current route functions for testing
class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]

# in main_app/views.py, do add this whether you're testing or not
def cats_index(request):
    context = {'cats': cats}
    return render(request, 'cats/index.html', context)

# in main_app/urls.py in urlpatterns
path('cats/', views.cats_index, name='index')


# in main_app/templates/base.html add link to cats index
<a href="/movies">Movies</a>

# in main_app/templates create cats folder
# in main_app/templates/cats create index.html
# in main_app/templates/cats/index.html
# setup block tags, add content
{% extends 'base.html' %}

{% block content %}

<h1>Cat List</h1>

{% for cat in cats %}
    <div class = "card">
        <div class = "card-content">
            <span class = "card-title">{{ cat.name }}</span>

            { if cat.age > 0 %}
                <p>Age: {{ cat.age }}</p>
            {% else %}
                <p>Age: Kitten</p>
            {% endif %}

        </div>
    </div>
{% endfor %}

{% endblock %}

# test, run server, 'python3 manage.py runserver'
# should be able to see list of cats on the index page, /cats

# git add and commit





""" SECTION 5 """
# create and reference erd.drawio file for models
# NOTE create your model correctly the first time
# in main_app/models.py
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
# this extends the Model class
# add all areas that you want


# connect model
# in terminal
# 'python3 manage.py makemigrations'
# should see 0001_initial.py in main_app/migrations NOTE do NOT change this file!
# run server, 'python3 manage.py runserver'
# should see message, 1 unapplied migration
# 'ctrl + c' to stop server
# 'python3 manage.py migrate' to migrate
# run server, 'python3 manage.py runserver'
# should see no migrations needed, main_app_cat should show in catcollectors db as a table

# NOTE reminder, when running server, make sure you are in the virtual environment, make sure it is active (reference lines 15-17)

# ANCHOR if you make changes and want to apply those changes, makemigrations again, and then migrate - repeat 299-308, in main_app/migrations should add new file 0002_initial.py


# to create an admin user for your site
# in terminal
# 'python3 manage.py createsuperuser'
# enter username, email, password, password

# run server, 'python3 manage.py runserver'
# test at localhost:8000/admin
# login with superuser credentials

# connect models to your admin users
# in main_app/admin.py
# add these two lines to grant access for this model
# underneath this line
# Register your models here.
from .models import Cat

admin.site.register(Cat)

# to override initial string method for Cat Model
# in main_app/models.py in class Cat underneath all fields, but make sure it is tabbed over and inside the class Cat
def __str__(self):
    return self.name

# git add and commit





""" SECTION 6 """
# to view all information from the database
# in main_app/views.py
# remove Cat class and list that was used for testing
# import Cat model from .models before this line
# Create your views here.
from .models import Cat
# in the def cats_index(request) add to first line
cats = Cat.objects.all()
# OR you could filter by doing
cats = Cat.objects.filter(name='Eldritch')
# all and filter will return lists, get will return one object, mostly just stick with the all()


# for the show individual element page
# in main_app/urls.py create a new route
path('cats/<int:cat_id>/', views.cats_detail, name='detail')
# make sure to add a comma after the previous path, or this one will not work

# add individual element path to views
# in main_app/views.py underneath cats_index function, you can also add this next comment in your code
# show
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    context = {'cat': cat}
    return render(request, 'cats/detail.html', context)
# this will show one cat for each id
# django uses ids starting at 1, not the 16 digit id code

# in main_app/cats create detail.html
# extend base.html
{% extends 'base.html' %}
{% block content %}
    # add cat info here
    <h1>Cat List</h1>

    <div>
        <span class = "card-title">{{ cat.name }}</span>

        { if cat.age > 0 %}
            <p>Age: {{ cat.age }}</p>
        {% else %}
            <p>Age: Kitten</p>
        {% endif %}

    </div>
{% endblock %}

# wrap divs in for loop (in main_app/cats/index.html) as anchor tags - links to show page
<a href="{% url 'detail' cat.id %}">
# considered django way of calling urls, stays up to date with changes

# run server and test, you should be able to see a list of cats on /cats/ page, and you should be able to click each item and be brought to another page
# 'python3 manage.py runserver'
# NOTE if you are having issues, make sure there are commas after all paths in main_app/urls.py, this is a list (like an array in js) and needs a comma after every object
# also make sure you have imported the correct model (Cat in this instance) in main_app/views.py
# also, if you don't see anything, go to /admin route and create something, our database is empty now and won't show anything unless we add something

# git add and commit





""" SECTION 7 """
# adding create route
# in main_app create forms.py
# in main_app/forms.py
from django.forms import ModelForm
from .models import Cat

class Cat_Form(ModelForm):
    class Meta:
        model = Cat
        fields = ['name','breed','description','age']
# fields should match class created in main_app/models.py
# they are not necessary, you can add whichever ones that you'd like (if user is in model, you wouldn't include that)


# in main_app/views.py
# underneath from .models import Cat
from .forms import Cat_Form

# in cats_index function, before context
cat_form = Cat_Form()
context = {'cats': cats, 'cat_form': cat_form}


# in main_app/templates/cats/index.html add form, make sure it is NOT in the for loop that you should already have in your index.html file
<form action="{% url 'index' %}" method="POST">
# this posts to the url with the name of index
    {% csrf_token %}
    {{ cat_form.as_p }}
    <input type="submit" value="Add Cat">
</form>
# the csrf_token is adding additional security, it's encrypting the value of our inputs, by default django will deny anything without this


# in main_app/views.py
# include redirect after render, it should be on the same line, just add a , redirect like so
from django.shortcuts import render, redirect
# we need to refactor our cats_index function
# this is the index && create route in one
# you can add this next line as a comment in your actual code above this function if you'd like
# index && create
def cats_index(request):
    if request.method == 'POST':
        cat_form = Cat_Form(request.POST)
        # the POST takes the data and fills out of the form
        if cat_form.is_valid():
            cat_form.save()
            # this will check that the data matches the model
            return redirect('index')
            # this is looking for a url with the name of index
    else:
        cat_form = Cat_Form()
    cats = Cat.objects.all()
    context = {'cats': cats, 'cat_form', cat_form}
    return render(request, 'cats/index.html', context)

# run server, 'python3 manage.py runserver'
# test, this should allow you to see the form, fill out the form, and see the new input on the index page after submitting the form
# this runs through our model and saves to our database

# git add and commit
# NOTE you can stay in virtual environment to add and commit





""" SECTION 8 """
# adding delete route
# in main_app/templates/cats/detail.html
# add edit and delete buttons under the cat fields
<a href="">Edit</a>
<a href="">Delete</a>

# in main_app/urls.py
# add new path in urlpatterns
path('cats/<int:cat_id>/delete', views.cats_delete, name="delete")
# reminder, all previous paths need commas or this route will not work

# in main_app/views.py add delete function underneath def cats_detail, you can also add this next comment in your code
# delete
def cats_delete(request, cat_id):
    Cat.objects.get(id=cat_id).delete()
    return redirect('index')
# this route will delete and redirect

# in main_app/templates/cats/detail.html
# in delete anchor tag
<a href="{% url 'delete' cat.id %}">Delete</a>

# run server, 'python3 manage.py runserver'
# test delete request, everything should be working now for CRD out of CRUD

# git add and commit





""" SECTION 9 """
# adding update and edit route
# if your server is running, you could probably stop it for now 'ctrl + c'
# in main_app/urls.py add new path in urlpatterns
path('cats/<int:cat_id>/edit', views.cats_edit, name='edit')
# don't forget your commas on paths!

# in main_app/views.py below the show route, you can also include the next comment for reference
# edit && update
def cats_edit(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    context = {'cat': cat}
    return render(request, 'cats/edit.html', context)


# in main_app/templates/cats create edit.html
# bring in base content
{% extends 'base.html' %}
{% block content %}
{% endblock %}

# add <h1>Edit {{ cat.name }}</h1> inside block
# in main_app/templates/cats/detail.html
# setup edit link where we set up our delete anchor tag in the previous section
<a href="{% url 'edit' cat.id %}">
# button should be working
# test this out, make sure everything is running on /edit
# run server, 'python3 manage.py runserver'


# add form inside block
# since we already have a working form for create, we can use that for the update form
# in main_app/views.py update the edit route we just added to include our form
def cats_edit(request, cat_id):
    cat = cat.objects.get(id=cat_id)
    cat_form = Cat_Form()
    context = {'cat': cat, 'cat_form': cat_form}
    return render(request, 'cats/edit.html', context)

# in main_app/templates/cats/edit.html setup form
# we always need two things in a form, 'csrf_token' for security and 'cat_form.as_p' that will generate all inputs and wrap them in p tags
<form action="" method="POST">
    {% csrf_token %}
    {{ cat_form.as_p }}
    <input type="submit" value="Update {{ cat.name }}">
</form>
# the form should now show on /edit

# in main_app/views.py
# update edit && update route, add instance in parameter of Cat_Form, this is the value from the db
def cats_edit(request, cat_id):
    cat = cat.objects.get(id=cat_id)
    # in form the instance = the object we pull back from the db
    cat_form = Cat_Form(instance=cat)
    context = {'cat': cat, 'cat_form': cat_form}
    return render(request, 'cats/edit.html', context)

# now add POST request, want to include instance again
def cats_edit(request, cat_id):
    cat = cat.objects.get(id=cat_id)
    if request.method == 'POST':
        cat_form = Cat_Form(request.POST, instance=cat)
        # we always want to check if it's valid here
        if cat_form.is_valid():
            cat_form.save()
            return redirect('detail', cat_id=cat_id)
    else:
        cat_form = Cat_Form(instance=cat)
    context = {'cat': cat, 'cat_form': cat_form}
    return render(request, 'cats/edit.html', context)

# in main_app/templates/cats/edit.html add action to form
<form action="{% url 'edit' cat.id %}" method="POST">
    {% csrf_token %}
    {{ cat_form.as_p }}
    <input type="submit" value="Update {{ cat.name }}">
</form>

# test everything with the edit route now
# we should have full CRUD
# git add and commit





""" SECTION 10 """
REVIEW
# one to many connection, how to add multiple connections
# NOTE reference erd.drawio for all models

# in main_app/models/py add new Feeding model
class Feeding(models.Model):
    date = models.DateField()
    # meal is going to be selection (B=breakfast, L=lunch, D=dinner) which is why max_length is 1
    meal = models.CharField(max_length=1)

# above the new class Feeding, add our selection of choices
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# now include MEALS in our class
# we can also set a default, current selection is MEALS index 0, index 0 = 'B'
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    # ForeignKey is the connection back to another table in our database
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='all_feedings')

    # override string
    def __str__(self):
        # if you have options in a charfield, django creates meal, this will display 'Breakfast' instead of 'B', .get_nameOfField_display()
        return f"{self.get_meal_display()} on {self.date}"
# on_delete is optional, but Dalton said we should always include it
# related_name is also optional, this creates a reverse connection on our cat, we can do cat.feeding to pull back our information, we could name this what we want, like all_feedings, later we can do cat.all_feedings.all() to pull back all feedings


# in terminal, migrate our new model
# 'python3 manage.py makemigrations'
# in main_app/migrations, there should be a new 000?_feeding.py file
# 'python3 manage.py migrate' to apply migration, you should be able to see this in database now


# connect our Feeding model to our admins
# in main_app/admin.py
# we just need to add Feeding after Cat for our import
from .models import Cat, Feeding
# underneath the admin.site.register(Cat), we need to add a new register for admin.site though
admin.site.register(Feeding)
# now if we login to localhost:8000/admin, we should see our model for our admins

# git add and commit





""" SECTION 11 """
REVIEW
# since we have connected our Feedings to our cats, we don't need to update our views.py
# in main_app/templates/cats/detail.html add feedings

# make sure the related name we set in main_app/models.py, which was related_name='all_feedings', is the same as our call in our for loop
# also, make sure to include '.all' after our name in our for loop so ALL feedings will be queried
<table class="striped">
    <thead>
        <tr>
            <th>Date</th>
            <th>Meal</th>
        </tr>
    </thead>

    <tbody>
        <!-- all_feeding = related name in model -->
        <!-- .all at the end is needed -->
        {% for feeding in cat.all_feedings.all %}
            <tr>
                <td>{{ feeding.date }}</td>
                <td>{{ feeding.get_meal_display }}</td>
            </tr>
        {% endfor %}

    </tbody>

</table>


# to reverse the sort order of our feedings we can include Meta class
# in main_app/models.py in our Feeding class
    class Meta:
        ordering = ['-date', 'meal']
        # adding 'meal' can also sort by meal type
# initial ordering is based on last modified in database


# in main_app/forms.py add our Feeding form
class Feeding_Form(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        # we don't want to include the cat field because we don't want the user to have to select

# in main_app/views.py
# import feeding form at top of views, just add Feeding_Form at the end of Cat_Form
from .forms import Cat_Form, Feeding_Form
# add feeding_form to our cats_detail function
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # SELECT * FROM cats WHERE id = cat_id
  context = {'cat': cat}
  feeding_form = Feeding_Form()
  context = {'cat': cat, 'feeding_form': feeding_form}
  return render(request, 'cats/detail.html', context)

# in main_app/templates/cats/detail.html add form
<form action="" method="POST">
    {% csrf_token %}
    {{ feeding_form.as_p }}
    <input type="submit" value="Add Feeding">
</form>
# now test, make sure to restart server


# add POST route to submit feeding to database
# in main_app/urls.py in urlpatterns
path('cats/<int:cat_id>/add_feeding', views.add_feeding, name='add_feeding')

# add route to views
# in main_app/views.py
def add_feeding(request, cat_id):
    pass

# change action to feeding form
# in main_app/templates/cats/detail.html

<form action="{% url 'add_feeding' cat.id %}" method="POST">
    {% csrf_token %}
    {{ feeding_form.as_p }}
    <input type="submit" value="Add Feeding">
</form>
# if we test this, we should get an error, didn't get an HttpResponse - didn't get back a return, could happen if we have pass or redirect


# in main_app/views.py change add_feeding function
def add_feeding(request, cat_id):
    feeding_form = Feeding_Form(request.POST)
    if Feeding_Form.is_valid():
        # if you need to manually add values to a form, commit = false return instanced db model but does not save to db
        new_feeding = feeding_form.save(commit=False)
        # assign the values
        new_feeding.cat_id = cat_id
        # commit that object to the db
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)
# if you want to associate the cat, we need to associate the new feeding to the cat_id, don't forget we ommitted our ForeignKey from our form

# now if we test this, we should see that adding a feeding to our cat updates our list of feedings


# adding model method
# in main_app/models.py add method funtion to Cat model
    def display_royal_name(self):
        return f"Your royal majesty {self.name}"
# now you have this function in views
# so if you want to add this in the detail.html, you can include this line instead of the name
{{cat.display_royal_name}}

# git add and commit





""" SECTION 12 """
REVIEW
# many to many relationships
# NOTE always reference erd.drawio for models
# in main_app/models.py add Toy model
# make sure to add new Toy model about Cat and Feeding classes
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# now add our toys field to our Cat model
    toys = models.ManyToManyField(Toy)
    # creates a join table, then when toys is accessed it searches the join table

# apply changes in terminal
# 'python3 manage.py makemigrations'
# 'python3 manage.py migrate'
# '\dt' to list 
# 'psql catcollector' you should see toys tables


# in main_app/admin.py
# add toy at the end of Feeding with just a ', Toy'
from .models import Cat, Feeding, Toy
# register Toy underneath current model registrations
admin.site.register(Toy)

# we can login to our admin portal for our site and add some toys to check
# once we've added those, we should be able to see a list of toys we've created when we view our cats


# to view toys that are associated with our cats
# in main_app/templates/cats/detail.html
# we can add a new section under everything else
<div>
    <h3>{{ cat.name }} Toys</h3>
</div>
# we should check our site, make sure that shows up the way that we want it
# back to main_app/templates/cats/detail.html
# NOTE it's always best to close else, endif, endfor stuff before adding content inside
<div>
    <h3>{{ cat.name }} Toys</h3>

    {% if cat.toys.count %}
        {% for toy in cat.toys.all %}
            <p>{{ toy.name }}</p>
            <p>{{ toy.color }}</p>
        {% endfor %}
    {% else %}
        <h5>No Toys</h5>
    {% endif %}

</div>
# now if we test our site, we should see our toys and their color


# now to see all toys that our cat does not have
# in main_app/views.py import our Toys, we can add it at the end of Cat with a ', Toys'
from .models import Cat, Toy
# in our show route (cats_details) add toys_cat_does_not_have variable and put it in our context
# TODO copy def cats_detail
# this selects all toys that does not have a relationship to cat_id

# in main_app/templates/cats/detail.html in our toys div
<div>
    <h3>Available Toys</h3>
    {% if toys.count %}
        {% for toy in toys.all %}
            <p>{{ toy.name }}</p>
            <p>{{ toy.color }}</p>
        {%endfor %}
    {% else %}
        <h5>{{ cat.name }} has all the available toys.</h5>
    {% endif %}
<div>
# now check our site, we should see all toys our cat has, and then all toys our cat does not have that are available

# in main_app/templates/cats/detail.html add form after our previous endif statement in available toys div
<form action="" method="POST">
    {% csrf_token %}
    <input type="submit" value="+">
</form>


# in main_app/urls.py add a path in urlpatterns
path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name="assoc_toy")

# in main_app/views.py create new route under everything else, can include next comment
""" Toy Routes """
def assoc_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('detail', cat_id=cat_id)
# in main_app/templates/cats/detail.html finish our form action so we can submit our form
<form action="{% url 'assoc_toy' cat.id toy.id %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="+">
</form>
# the order that you pass the arguments in should be the order that you plass them in url for form action
# now if we test on our site, we can hit the plus button and the toy will be added to the list of cat's toys


# we can also do the same thing to remove our toy
# in main_app/views.py add a new deassoc function for our toy route to remove our toy_id
def deassoc_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect('detail', cat_id=cat_id)

# in main_app/urls.py add a path in urlpatterns that is the same as our assoc_toy but now has the deassoc_toy function
path('cats/<int:cat_id>/deassoc_toy/<int:toy_id>/', views.deassoc_toy, name="deassoc_toy")

# in main_app/templates/cats/detail.html we can add a new form to our toys that are linked to our cat that will deassoc_toy
<form action="{% url 'deassoc_toy' cat.id toy.id %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="-">
</form>

# test site, we should be able to fluidly add and remove toys associated with our cat
# git add and commit





""" SECTION 13 """
REVIEW
# authentication
# our relationship will be one to many, one user to many cats, you could do many to many, but not this time
# in main_app/models.py import user model at the very top
from django.contrib.auth.models import User
# in our Cat class under our other fields we can include our user field
user = models.ForeignKey(User, on_delete=models.CASCADE)
# we want to always include on_delete, this will protect our database

# if we try to migrate or makemigrations now, we will run into issues with data that already exists in our database
# in terminal
# 'python3 manage.py makemigrations'
# if we see 'Provide a one-off default now', select either '1' or '2', probably '1'
# will show enter default value as valid Python
# enter '1' because we already have our admin superuser that we created earlier
# now we can migrate
# 'python3 manage.py migrate'
# running server should show no issues now
# we can see in our site admin side that we have users and a user associated with every cat


# we don't want our users to login through the admin page, we want to create a login form
# in catcollector_project/urls.py we want to include our path to auth
# in our urlpatterns, include a new path, don't forget commas
path('accounts/', include('django.contrib.auth.urls'))

# in main_app/templates create new folder registration
# in main_app/templates/registration create login.html and add base content
{% extends 'base.html' %}
{% block content %}

    <h1>Log In</h1>

    <form action="" method="POST">

        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="login">
        <input type="hidden" name="next" value="{{next}}">

    </form>

{% endblock %}
# now if we view our site at accounts/login, we should see our Log In h1 tag
# adding our hidden input will give our form somewhere to redirect
# we shouldn't be able to log in yet, django automatically tries to redirect to a profile page, but we don not have one

# in catcollector_project/settings.py at the very bottom add our login redirect
LOGIN_REDIRECT_URL = '/cats/'
# now if we test our site, it will redirect to our cats dashboard


# we want to control what our user sees when they are not logged in vs when they are
# in main_app/templates/base.html
# we can add login or logout button in our nav
{% if user.is_authenticated %}
    <li><a href="{% url 'index' %}">All Cats</a></li>
    <li><a href="{% url 'logout' %}">Logout</a></li>
{% else %}
    <li><a href="{% url 'login' %}">Login</a></li>
    <li><a href="{% url 'signup' %}">Signup</a></li>
{% endif %}
# if we try to logout now, django will redirect to our django admin, but that's not what we want

# in catcollector_project/settings.py at the very bottom add our logout redirect
LOGOUT_REDIRECT_URL = '/'


# in main_app/views.py update index && create function
# tells form not to commit right away, takes cat and accesses the user, then saves the user to that cat
# TODO copy new function
# now we can verify this works on our site by adding a cat
# if we go to our new cat on our admin site, we can see our user is linked to the cat now


# next we want to only show cats that are associated with individual users
# in main_app/views.py we want to filter cats that have a user in request
# TODO update index && create with the filter
# test our site, our user should only show their cat
# toys is still all available, we could do the same thing with user association for toys


# last thing we need for auth is a signup page
# we should first logout of our site
# in main_app/urls.py add new path
path('accounts/signup', views.signup, name="signup")

# in main_app/views.py import external import at the very top under render and HttpRes
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# add new auth route at the very bottom
""" Auth Routes """
def signup(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)

# in main_app/templates/registration create signup.html
{% extends 'base.html' %}
{% block content %}
    <h1>Sign Up</h1>

    <form action="{% url 'signup' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
    </form>
{% endblock %}

# in main_app/views.py update our signup route
def signup(request):
    if request.methor == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)
# we should now be able to register a new user

# in main_app/views.py we can add an error message to our user auth route
def signup(request):
    error_message = ''
    if request.methor == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid signup please try again'
    else:
        form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# in main_app/templates/registration/signup.html we can add our error message
{% if error_message %}
    <p>{{ error_message }}</p>
{% endif %}
# we can place this wherever we'd like
# this will work, we could also go in to deeper django to do more, this was just additional error messages


# safe guarding our routes from users that aren't logged in
# in main_app/views.py at the very top in our external imports section
from django.contrib.auth.decorators import login_required
# for whatever functions/routes that we want to be visible only for users that are logged in, we just put this line directly before our function
@login_required
# pretty much anything but our signup route


# in main_app/views.py we can hide any cats that are not associated with our user underneath our cat = Cat.objects
if cat.user != request.user:
    return render(request, 'cats/notYourCat.html', {'cat': cat})

# we should have full login and register auth for our users
# git add and commit