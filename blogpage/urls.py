from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='singlepost'),
    path('<slug:slug>/', views.post_detail, name='singlepost')
]