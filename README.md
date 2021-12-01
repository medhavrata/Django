# Django
This repo is to build a Djano app

This repo is to build a Djano app

    Install Django

    pip3 install django

    Next, start a new project

    django-admin startproject password_generator

    Go to password_generator directory and run: python3 manage.py runserver, and it will run the default server
    When we execute the 'django-admin startproject password_generator' command, django will create a directory with name password_generator. Inside this, there will be another directory named password_generator(having more files inside), a file manage.py, another file db.sqlite3
    We can rename the top level directory to password_generator_project so that we know this is the top level project
    Django project is the complete website and inside this website we can have many Applications, which represent a separte functionality of the website.
    run the command 'python3 manage.py startapp generator' to create an application inside the project
