## Steps to run project
### Step One
#### Clone Project
```commandline
git clone -b dev.1.0.0 https://github.com/nhridoy/django-coding-test-master.git
```
#### Install Pipenv
```commandline
pip install pipenv
```
#### Navigate to Folder
```commandline
cd django-coding-test-master
```
#### Install Packages
```commandline
npm install
```
```commandline
pipenv install
```
or using your installed python version
```commandline
pipenv install --python=3.10
```
#### Generate Static Files
```commandline
npm run watch
```
#### Activate Virtual Environment
```commandline
pipenv shell
```
#### Open Project Folder
```commandline
cd src
```
#### Makemigrations, Migrate and Createsuperuser
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
```commandline
python manage.py createsuperuser
```
#### Start server
```commandline
python manage.py runserver
```
### This project is using SQLite Database
#### Current Admin username and password is
```
admin
```
```
admin
```