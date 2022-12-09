from django.shortcuts import render

projects_list = {
    "Unifesp Tables": [
        "python, Pandas, tabula-py, openpyxl",
        "/link"
        ],
    "Classes API": [
        "python, Django RestFramework, Postman, MySQL",
        "/link"
        ],
    "IMDb Prediction Algorithm": [
        "python, Machine Learning",
        "/link"
        ],
    "My Website": [
        "python, Django Framework, HTML, CSS, JS",
        "/link"
    ]
}

# Create your views here.
def index(request):
    my_projects = projects_list.items()
    # return HttpResponse("Hello World! This is My Hobbies webpage!")
    return render(request, "home/index.html", {
        "projects": my_projects
    })

