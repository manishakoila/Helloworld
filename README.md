# Building Helloworld Django App
## Step1-Checking Django version
check whether django is installed in your system by using below command:

```python -m django --version```
if django not installed in your pc use below command to install django

```pip install django```

## Step2-creating project
by using cd command change the destination folder at where project has to be stored then use the below command to create "HelloWorld" Application.

```python -m django startproject Helloworld```

by running the above command you can observe a "Helloworld" folder is created in your destination folder , which contains below  files
```
    manage.py
    HelloWorld/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
## Step-3 Running Server 
Now Navigate to the Helloworld folder using "cd Helloworld" and run below command to run the server

```py manage.py runserver```

After running you observe output in cmd as follows:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 26, 2024 - 18:49:59
Django version 5.0.4, using settings 'Helloworld.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```
Now  visit http://127.0.0.1:8000/ with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off evident that django app is running successfully

## Step-4 creating pools app
 In same folder run below command to create a DjangoApp:

``` py manage.py startapp DjangoApp ```

After running above command you can observe a new "DjangoApp" folder is created, which contains the below files

```
DjangoApp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
## Step-5 Adding html template
Now create a folder named "templates" in DjangoApp folder, in that folder create a html file named hello.html, in that file add code given below
``` html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1><strong>{{message}}</strong></h1>
</body>
</html>
```

## Step-6: Adding code in views.py

Now we need to modify the views.py file code in DjangoApp folder as follows:
``` python
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    if request.GET.get('format') == 'html':
        return render(request, 'hello.html', {'message': 'Hello World!'})
    return JsonResponse({"Message": "Hello World!"})
```
## Step-7: create urls.py file in DjangoApp folder
Now create a "urls.py" python file and add the following code in it
``` python
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='index'),  
]
```
## Step-8: Modify urls.py file in Helloworld folder
Now modify HelloWorld/urls.py file as follows
``` python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('DjangoApp/', include('DjangoApp.urls')),
    path('admin/', admin.site.urls),
]
```
## Step-9 Running Server
Now run the server again by using command

```py manage.py runserver```
### For Json output
Now go to "http://localhost:8000/DjangoApp/ " website it shows the json output as follows:

```
{"Message": "Hello World!"}

```
### For HTML output
Now go to "http://localhost:8000/DjangoApp/?format=html " website it shows the html output as follows:


# Hello World!









