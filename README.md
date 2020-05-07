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