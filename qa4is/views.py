from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Industry

def industry_list(request):
    industries = Industry.objects.all()

    #get model fields

    field_names = [field.name for field in Industry._meta.get_fields()
                   if not field.is_relation and not field.name.startswith('_')]
    context = {
        'industry': industries,
        'field_names': field_names,
    }

    return render(request, 'industries/industry_list_alt.html, context')


def home(request):
    return render(request, 'home.html')  # Ensure you have a `home.html` template

def about(request):
    return render(request, 'about.html')
