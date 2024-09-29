from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    if request.GET.get('format') == 'html':
        return render(request, 'hello.html', {'message': 'Hello World!'})
    return JsonResponse({"Message": "Hello World!"})

