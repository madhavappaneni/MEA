from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import render
from .models import ProfileModel

def home(request):
    template = 'profiles/home.html'
    return render(request, template, context=None)
def profile_detail_view(request, pk):
    try:
        p = ProfileModel.objects.get(pk=pk)
    except ProfileModel.DoesNotExist:
        raise Http404("Profile Model Does Not Exists")
    template = 'profiles/detail.html'
    context = {"profile":p}
    return render(request,template,context)

def profile_list_view(request):
    profile_list = ProfileModel.objects.all()
    template = 'profiles/list.html'
    context = {'profile_list':profile_list}
    return render(request,template,context)

def contact(request):
    template = 'profiles/contact.html'
    return render(request, template, context=None)

