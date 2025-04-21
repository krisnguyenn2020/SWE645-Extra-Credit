from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Survey
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .forms import SurveyForm


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
        email = request.POST.get('email')
        if Survey.objects.filter(email=email).exists():
            messages.error(request, "Survey already submitted with this email.")
            return redirect('submit_form')  # Or wherever you want to redirect
        # Save the new survey
        Survey.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            street_address=request.POST.get('street_address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            zip=request.POST.get('zip'),
            telephone_number=request.POST.get('telephone_number'),
            email=email,
        )
        messages.success(request, "Survey submitted successfully!")
        return redirect('survey_list')
    return render(request, 'survey_app/survey_form.html')


def update_survey_by_id(request, id):
    survey = get_object_or_404(Survey, id=id)
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=survey)
        if form.is_valid():
            form.save()
            return redirect('survey_list')
    else:
        form = SurveyForm(instance=survey)
    return render(request, 'survey_app/survey_form.html', {'form': form, 'update': True})

def delete_survey_by_id(request, id):
    try:
        survey = Survey.objects.get(id=id)
        survey.delete()
        messages.success(request, "Survey deleted successfully.")
        return redirect('survey_list') 
    except Survey.DoesNotExist:
        messages.error(request, "Survey not found.")
        return redirect('survey_list')  

def view_survey_detail(request, id):
    survey = get_object_or_404(Survey, id=id)
    return render(request, 'survey_app/survey_detail.html', {'survey': survey})

def survey_list(request):
    surveys = Survey.objects.all().order_by('-date_of_survey')
    return render(request, 'survey_app/survey_list.html', {'surveys': surveys})
