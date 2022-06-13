# Simple FileUpload App

## Upload a file
Currently, supports only csv file

### Set up
    - pip install -r requirements.txt
    - python manage.py migrate
    - sudo service redis-server start
    - python manage.py rqworker
    - python manage.py runserver

#### Key libraries
    - django
    - django-rq
    - redis
    - django_fsm


##### Task checklist
    - File Upload API (DONE)
    - Tests for File Upload API (IN PROGRESS)

###### API endpoints
    - /uploads/ - Create a new upload
    - /uploads/<id>/ - Get a specific upload
