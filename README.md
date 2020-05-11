# django-fundamentals
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![course-project](https://img.shields.io/badge/Project-Course-orange.svg)

Exercise of the Pluralsight course: Django Fundamentals by Reindert-Jan Ekker


## Built With
<a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/BorjaG90/media/master/img/logos/python.png" width=50 alt="Python 3.6.1"></a>
<a href="https://www.djangoproject.com/"><img src="https://raw.githubusercontent.com/BorjaG90/media/master/img/logos/django.png" width=50 alt="Django 2.1.5"></a>
<a href="https://developer.mozilla.org/es/docs/HTML/HTML5"><img src="https://raw.githubusercontent.com/BorjaG90/media/master/img/logos/HTML5.png" width=50 alt="HTML5"></a>
<a href="https://developer.mozilla.org/es/docs/Web/CSS"><img src="https://raw.githubusercontent.com/BorjaG90/media/master/img/logos/css3.png" width=50 alt="CSS3"></a>
<a href="https://getbootstrap.com/"><img src="https://raw.githubusercontent.com/BorjaG90/media/master/img/logos/bootstrap.png" width=50 alt="Bootstrap"></a>
<a href="https://code.visualstudio.com/"><img src="https://raw.githubusercontent.com/BorjaG90/media/master/img/logos/vscode.png" width=50 alt="VSCode"></a>


# django_getting_started
    django-admin startproject meetingplanner

#####   To link & create html to core project where views are linked in urls of coreproject
    python manage.py startapp website

- Add 'website' in INSTALLED_APPS of settings.py in meetingplanner
- Check URL mapping in urls.py file in meetingplanner if your url getting 404


##### Python Data Model & Migration
Data Model is actually a table of database. In other words, it linked to the database.
Migration is concept which keep the database up to date with whatever changes you have done in code and data model classes
- To see pending migration
        
         python manage.py showmigrations
- To run migration

         python manage.py migrate
         
##### Created Meeting Data Model
After creating Model class, you have to generate migration files to which later on migrate in database later on.

    python manage.py makemigrations

This commands create migration scripts under migrations/ folder.

To see the SQL syntax of our created Model, execute the following command

    python manage.py sqlmigrate meetings 0001
Here, 0001 is the index of our migration file under the meetings/migrations. folder.
Now run the migrate commnad to apply the changes in the database.


##### To create, edit data from inbuilt admin panel.
We have to configure the admin mapping in admin.py file.
To use the inbuilt admin panel, we required to create one super user.

##### To create super user
    python manage.py createsuperuser


##### Flow of django MTV (Model, Template, View) [MVC] pattern
<img src="./screenshots/flow.png" alt="Original"  align="middle"/>


#### Template supports inline code like JSTL
To show any value from context or dictionary, We need to use.

    {{object.value}}

To iterate through list of object, there is support of forloop also, but it is inside the code block like below.

    {% for item in items %}
    -----
    {% endfor %}

##### URL Mapping
To create url mapping of each html pages dynamically, We have to provied <b>name</b> attribute to 
url's path method in urls.py like below.

        path('<int:id>', detail, name='detail'),

Now if we need to call the detail page from any html templat, We just need to call

       <a href="{% url 'detail' meeting.id %}">{{meeting.title}}</a>
    
which bind the detail view page and also overloading the meeting.id param to <int:id>.

Still applying url binding in main general project's urls.py is so much repetitive task so django provides
a solution to this by seprating module's urls in module's urs.py and including this urls in general urls.py like below.

    from django.urls import path, include
    path('meetings/', include('meetings.urls'))

where meetings.urls targetting the urls.py file of meeting module.


##### Applying Template Inheritance and providing static content.
To apply template inheritance concept, We need to create one base html under the templates directory.
This base.html contains the command layout using following code.

    {% block content %} {% endblock %] 

Above lines are just declaration like where the all content of page goes according to base,html.
After above declation, We have to specify following code to all html files to make the template common and standard.

    {% extends 'base.html' %} #first line
    {% load static %} #Mandatory line to load static content with following code
    {% static 'module/style.css' %}

The above extend line is required to inherit template design.
then we have to place our body code under 
    
    {% block conten %} ...body... {% endblock %}
    