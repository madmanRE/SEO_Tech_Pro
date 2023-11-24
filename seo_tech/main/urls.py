from django.urls import path
from .views import index, get_form, admin, admin_detail_view

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("get_form/", get_form, name="get_form"),
    path("admin_view/<int:pk>/", admin_detail_view, name="admin_detail_view"),
    path("admin_view/", admin, name="admin"),
]
