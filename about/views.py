from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello World! This is My Hobbies webpage!")
    return render(request, "about/index.html")
