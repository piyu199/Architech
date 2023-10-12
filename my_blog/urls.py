from django.urls import path
from . import views

urlpatterns = [
    path('blog_home/',views.blog_home,name='blog_home'),
    path('article/<int:pk>',views.article_view,name='article'),
    path('create/',views.create,name='create'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path("blogs/",views.blog_list,name='blog_list'),
    path("blogs_details/<int:pk>",views.blog_details,name='blog_details'),
]
