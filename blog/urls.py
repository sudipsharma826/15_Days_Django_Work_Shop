from django.urls import path
from .views.main_views import home,create_blog,single_blog,edit_blog,delete_blog
from .views.auth_views import register,login

urlpatterns = [
    path("", home, name="home"), 
    path("register/", register, name="register"), 
    path("login/", login, name="login"), 
    path("create/", create_blog, name="create_blog"), 
    path("<int:blog_id>/", single_blog, name="single_blog"), 
    path("edit/<int:blog_id>/", edit_blog, name="edit_blog"),  # Added missing comma
    path("<int:blog_id>/delete/", delete_blog, name="delete_blog")  # Added trailing slash for consistency
]
