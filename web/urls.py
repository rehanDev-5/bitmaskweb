from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="homepage"),
    path('',views.index, name="homepage"),
    path('blog/',views.blogs_avail, name="pageblogs"),
    path('blog/<int:pk>/',views.blog_page, name="blogpage"),
]