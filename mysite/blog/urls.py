<<<<<<< HEAD
from django.contrib.auth import login, logout
from django.urls import path
from . import views
from .feeds import LatestPostsFeed
from django.contrib.auth.views import logout_then_login, LoginView

app_name = 'blog'


urlpatterns = [
=======
from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
>>>>>>> be8bda85bcc865affa2b67d8e65a6c9ffd05e4d7
    path('',views.PostListView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
<<<<<<< HEAD
    path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    # path('register/', views.register, name='register'),
]

=======
]
>>>>>>> be8bda85bcc865affa2b67d8e65a6c9ffd05e4d7
