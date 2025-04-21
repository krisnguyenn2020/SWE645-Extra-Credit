"""
URL configuration for student_survey project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save/', views.save_survey, name='save_survey'),                   # POST
    path('all/', views.get_all_surveys, name='get_all_surveys'),           # GET
    path('<int:id>/', views.get_survey_by_id, name='get_survey_by_id'),    # GET
    path('<int:id>/delete/', views.delete_survey_by_id, name='delete_survey'),  # DELETE
    path('<int:id>/update/', views.update_survey_by_id, name='update_survey'),  # PUT
]
