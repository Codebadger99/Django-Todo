"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from List.views import todo_home_view,update_task_view,delete_task_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_home_view, name='home'),
    path('update/<int:pk>/', update_task_view, name='update'),
    path('delete/<int:pk>/', delete_task_view, name='delete')
]
