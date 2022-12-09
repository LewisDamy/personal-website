from django.urls import path

from . import views

urlpatterns = [
    path("", views.index)
    # path("<int:project>", views.projects_list_by_number),
    # path("<str:project>", views.project_list, name="projects-list")
]


