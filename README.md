project-management
=================

What is Project Management?
---------------------------
Project management is a django application built using django admin interface. The application can be used to manage
software development projects for different teams in a company.

How can I get Project Management?
---------------------------------
If you are familiar with django setup and architecture, just clone this repository, run migrations, start the web server
and go the admin site. If you are not familiar with django then go to
[https://docs.djangoproject.com/en/dev/intro/tutorial01/](https://docs.djangoproject.com/en/dev/intro/tutorial01/) to
learn how to use this application.

OK I cloned it. What's next?
----------------------------
After you clone the repository you have to do the following steps to get it working:
* If you are using `virtualenv` create a new virtual environment for this project, activate it and run
`pip install -r requirements.txt` from under the project folder. This will install all the packages required to run
this application.
* See `settings.py` file under pm app and create database and change the connection parameters.
* Run `syncdb` and `python manage.py migrate` to migrate tables to database
* Run `python manage.py runserver 0.0.0.0:4000` and open your browser and hit http://localhost:4000/admin


