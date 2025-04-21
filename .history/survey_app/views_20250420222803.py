from django.shortcuts import redirect, render
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

@csrf_exempt
def update_survey_by_id(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            survey = Survey.objects.get(id=id)

            for key, value in data.items():
                setattr(survey, key, value)

            survey.save()
            return JsonResponse({'message': 'Survey updated', 'survey': model_to_dict(survey)})

        except Survey.DoesNotExist:
            return JsonResponse({'error': 'Survey not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# Create your views here.from django.shortcuts import render, redirect
from .models import Survey

def submit_form(request):
    if request.method == 'POST':
        Survey.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            street_address=request.POST.get('street_address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            zip=request.POST.get('zip'),
            telephone_number=request.POST.get('telephone_number'),
            liked_most=request.POST.get('liked_most'),
            interest_source=request.POST.get('interest_source'),
            recommendation=request.POST.get('recommendation'),
        )
        return redirect('survey_list')

    return render(request, 'survey_app/survey_form.html')


def survey_list(request):
    surveys = Survey.objects.all().order_by('-date_of_survey')
    return render(request, 'survey_app/survey_list.html', {'surveys': surveys})
