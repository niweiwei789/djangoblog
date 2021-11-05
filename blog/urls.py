from django.urls import path,re_path

from . import views

app_name = 'blog'
urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    #re_path('archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.ArchivesView.as_view(), name='archives'),
    path('archives/<int:year>/<int:month>/', views.ArchivesView.as_view(), name='archives'),
    path(r'category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path(r'tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    # path(r'^search/$', views.search, name='search'),
]
