from django.urls import path
from blogging.views import stub_view, list_view, detail_view, add_view

urlpatterns = [
    path('', list_view, name='blog_index'),
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
    path('posts/add/', add_view, name='blog_add'),
]
