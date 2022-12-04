# Django Forms and Formsets

This repository contains the source code for [Make Amazing Django Form and Formset [in 7 Steps]](https://medium.com/@fatemefuoladkar/amazing-django-form-and-formset-in-7-steps-6b692d5a2032) Tutorial on Medium. 

## How to run the project 
### **On Windows**:

Open the terminal (cmd, powershell, git bash, ...) and:

#### Clone the repository
```
git clone https://github.com/FatemeFouladkar/Django-Forms-and-Formsets.git
```

#### Set up virtual environment
``` 
pip install virtualenv       # install virtualenv
virtualenv .venv             # make a virtualenv (in the project's directory)
.venv/Scripts/Activate.ps1   # activate the virtualenv
```

#### Install the dependencies 
```
pip install -r requirements.txt
```

#### Run the project
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
-----------------------

### **On Linux**:

Open the terminal and:

#### Clone the repository
```
git clone https://github.com/FatemeFouladkar/Django-Forms-and-Formsets.git
```

#### Set up virtual environment
``` 
pip install virtualenv       # install virtualenv
virtualenv .venv             # make a virtualenv (in the project's directory)
source .venv/bin/activate    # activate the virtualenv
```

#### Install the dependencies 
```
pip install -r requirements.txt
```

#### Run the project
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```