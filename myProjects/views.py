from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

projects_list = {
    "Unifesp Tables": [
        "This is an Python project that allows students to analyse the subjects in a more succinct format",
        "images/4.png"
        ],
    "Classes API": [
        "The REST API is the continuation of the tables project that were convertend in a backend tool",
        "images/6.png"
        ],
    "IMDb Prediction Algorithm": [
        "Final project from Artificial Intelligence Subject in which we've used KNN and Linear Regression to predict the rating from IMDB movies",
        "images/13.png"
        ],
    "My Website": [
        "Customized Django Website, using HTML, CSS and Python",
        "images/11.png"
    ]
}


# Create your views here.
def index(request):
    my_projects = projects_list.items()
    return render(request, "myProjects/index.html", {
        "projects": my_projects     # render this list
    })

def projects_list_by_number(request, project):
    my_projects = list(projects_list.keys())  # list of projects from dict

    if project > len(my_projects):
        return HttpResponseNotFound("Invalid Project!")

    redirect_project = my_projects[project - 1]
    redirect_path = reverse("projects-list", args=[redirect_project])
    return HttpResponseRedirect(redirect_path)

def project_list(request, project):
    try:
        project_text = projects_list[project]
        content_text = projects_list[project][0]
        image_location = projects_list[project][1]
        return render(request, "myProjects/includes/project.html", {
            "text": project_text,
            "img_path": image_location,
            "content": project,
            "content_text": content_text
        })
    except:
        raise Http404()
