from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<str:title>',views.page_view, name='page_view'),
]
