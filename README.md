# PicsAgram
An 'Instragram-ispired' Single Page Application built with Django, Django Rest Framework and Vue JS

## Hot to set up the project to run on your local machine?
 Download the code to your PC, unpack the zip and move inside the folder.
Create a new Python Virtual Environment:

```
py -m venv venv
```
Activate the environment and install all the Python/Django dependencies:

```
cd/venv/scripts
activate
pip install -r requirements.txt
```
Apply the migrations as usual.

Time to install the Vue JS dependencies:
```
cd picsagram/frontend
npm install
```
Run Vue JS Development Server:
```
npm run serve
```
Run Django's development server:
```
python manage.py runserver
```
Open up Chrome and go to 127.0.0.1:8000 and the app is now running in development mode!


### Built With

* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Vue JS](https://vuejs.org/)
