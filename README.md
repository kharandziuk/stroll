- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py
- pip install virtualenv
- virtualenv -p $(which python3) ENV
- ./manage.py migrate
- ./manage.py createsuperuser
- ./manage.py runserver
- then open http://localhost:8000/admin and create some venues
- then open http://localhost:8000/venues
