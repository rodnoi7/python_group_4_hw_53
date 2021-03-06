"""trecker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import IssueListView, IssueDetailView, IssueCreateView, IssueDeleteView, IssueUpdateView, TypeListView, TypeCreateView, StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView, TypeDeleteView, TypeUpdateView, ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectDetailView, DeactiveProjectListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IssueListView.as_view(), name='index'),
    path('issue_view/<int:pk>', IssueDetailView.as_view(), name='view'),
    path('issue/create', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='del_issue'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update'),
    path('types', TypeListView.as_view(), name='type_list'),
    path('type/create', TypeCreateView.as_view(), name='add_type'),
    path('status', StatusListView.as_view(), name='status_list'),
    path('status/create', StatusCreateView.as_view(), name='add_status'),
    path('status/<int:pk>/update', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete', StatusDeleteView.as_view(), name='del_status'),
    path('type/<int:pk>/update', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete', TypeDeleteView.as_view(), name='del_type'),
    path('projects', ProjectListView.as_view(), name='project_list'),
    path('project_view/<int:pk>', ProjectDetailView.as_view(), name='project_view'),
    path('project/create', ProjectCreateView.as_view(), name='add_project'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='del_project'),
    path('deactive/projects', DeactiveProjectListView.as_view(), name='deactive_projects'),
]
urlpatterns += staticfiles_urlpatterns()