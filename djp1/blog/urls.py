from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    BloodPostListView,
    OrgansUserPostListView,
    OrgansPostListView,
    OrgansPostDetailView,
    OrgansPostCreateView,
    OrgansPostUpdateView,
    OrgansPostDeleteView,
    BloodPostDetailView,
    BloodPostCreateView,
    BloodPostUpdateView,
    BloodPostDeleteView,
    BloodUserPostListView,
    
    )
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('blood/', BloodPostListView.as_view(),name='blood-home'),
    path('organs/', views.organs,name='organs-home'),

    path('blood/<str:username>', BloodUserPostListView.as_view(),name='blood-user-posts'),
    path('blood/<int:pk>/', BloodPostDetailView.as_view(),name='blood-post-detail'),
    path('blood/new/', BloodPostCreateView.as_view(),name='blood-post-create'),
    path('blood/<int:pk>/update/', BloodPostUpdateView.as_view(),name='blood-post-update'),
    path('blood/<int:pk>/delete/', BloodPostDeleteView.as_view(),name='blood-post-delete'),
    

    path('organs/', OrgansPostListView.as_view(),name='organs-blog-home'),
    path('organs/<str:username>', OrgansUserPostListView.as_view(),name='organs-user-posts'),
    path('organs/<int:pk>/', OrgansPostDetailView.as_view(),name='organs-post-detail'),
    path('organs/new/', OrgansPostCreateView.as_view(),name='organs-post-create'),
    path('organs/<int:pk>/update/', OrgansPostUpdateView.as_view(),name='organs-post-update'),
    path('organs/<int:pk>/delete/', OrgansPostDeleteView.as_view(),name='organs-post-delete'),
    
    path('about/', views.about,name='blog-about'),
    path('contact/', views.contact,name='blog-contact')
]

