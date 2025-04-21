from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.submit_form, name='submit_form'),
    path('list/', views.survey_list, name='survey_list'),

    path('save/', views.save_survey, name='save_survey'),
    path('all/', views.get_all_surveys, name='get_all_surveys'),
    path('<int:id>/', views.get_survey_by_id, name='get_survey_by_id'),
    path('<int:id>/delete/', views.delete_survey_by_id, name='delete_survey'),
    path('<int:id>/update/', views.update_survey_by_id, name='update_survey'),
]
