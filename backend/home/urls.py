from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("api/", views.Home2.as_view(), name="person-create"),
    path("api/edit/<int:person_id>/", views.EditPeople.as_view(), name="person-edit"),
    path(
        "api/delete/<int:person_id>/",
        views.Home2.as_view(),
        name="person-delete",
    ),
]
