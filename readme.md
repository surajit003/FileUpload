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

###### Design flow
    - File Upload design
        - file_upload_design.png

###### API endpoints
    - /uploads/ - Create a new upload
    - /uploads/<id>/ - Get a specific upload

###### Explanation of the choice of technology
    - Django - For rapid bootstraping of the app
    - Django-RQ - For asynchronous processing of the app
    - redis - queue
    - django_fsm - state machine
       
###### API design
When a request is sent to the upload endpoint, a new upload is created if the
initial header check is successful. If the header check fails then the user
is redirected to the upload detail page for further instructions.

If the header check is successful, a new upload is created and the upload
status is set to PENDING. Once, the upload is saved then a post_save signal
is trigerred to start the processing of the upload. The upload status is now
set to PROCESSING. The post_save signal adds the task to the default queue and
the request-response thread is completed.

Once, the task is added to the queue, there are workers listening to the queue
who then picks up the task and processes it. Inside the processing handler, the
file is then read and the objects are created/updated in the database. If there is
an exception in a row then the error details are appended to upload record and the
processing continues until it reaches the end of the file.

Once the reading of the file is complete, the upload status is set to COMPLETE.

### Improvements
    - Instead of committing each record one by one, we should leverage the django-ORM's
      ability to bulk create/update records.
    - We should add a progress bar for the upload status to show the user how much of the upload is complete.
    - We should also fine tune the FE and make it more user friendly.


