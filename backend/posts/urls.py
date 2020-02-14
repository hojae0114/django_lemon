from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('photos/<int:photo_id>', views.photo_list),
]
