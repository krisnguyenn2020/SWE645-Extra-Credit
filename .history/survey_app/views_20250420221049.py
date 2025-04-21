from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Survey
from django.forms.models import model_to_dict
import json

@csrf_exempt
def save_survey(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        survey = Survey.objects.create(**data)
        return JsonResponse({'message': 'Survey saved', 'id': survey.id})

@csrf_exempt
def get_all_surveys(request):
    if request.method == 'GET':
        surveys = list(Survey.objects.values())
        return JsonResponse(surveys, safe=False)

@csrf_exempt
def get_survey_by_id(request, id):
    try:
        survey = Survey.objects.get(id=id)
        return JsonResponse(model_to_dict(survey))
    except Survey.DoesNotExist:
        return JsonResponse({'error': 'Survey not found'}, status=404)

@csrf_exempt
def delete_survey_by_id(request, id):
    try:
        survey = Survey.objects.get(id=id)
        survey.delete()
        return JsonResponse({'message': 'Survey deleted'})
    except Survey.DoesNotExist:
        return JsonResponse({'error': 'Survey not found'}, status=404)

# Create your views here.
