# Event-management-with-Django


### Steps to run

#### Step One  : Run migrations
python manage.py migrate

#### Step Two :
python manage.py runserver


### Django url - controller - template pattern
1) all urls are located in urls.py [pattern : <url>, views.function, url name]
2) functions are defined in views.py -> controller
3) templates are defined in templates -> html files

#### Note: main functions defined in views.py to return an html
    - render(request, <tempalte-name>, context [must be a dict]
    - redirect(request,<url name>

#### Note: django does not have HTTP method based routing, so all routes will point to same method
#### use condition to perform action based on HTTP method

# BAKI SAAB CHAT GPT
   
