# create a new virtual environment
```
python3 -m venv env/myshop
```

# activate your virtual environment
```
source env/myshop/bin/activate
```

# deactivate your virtual environment
```
deactivate
```

# startup project
```
django-admin startproject myshop
```

# new application 
```
cd myshop/
django-admin startapp shop
```

# initial migrations database
```
python3 manage.py makemigrations
```

# sync the database
```
python3 manage.py migrate
```

# create super user
```
python3 manage.py createsuperuser
```

# run development server / different port
```
python3 manage.py runserver

python3 manage.py runserver 8080