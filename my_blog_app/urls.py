from django.urls import path

from . import views

app_name = "my_blog_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:slug>/', views.post_page, name="post_detail"),
]