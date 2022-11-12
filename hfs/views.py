from django.http import HttpResponse
from django.shortcuts import render
from apps.users.models import Profile


def landing(request):
    #return HttpResponse("landing")
    profiles = Profile.objects.all()
    return render(request, 'core/pages/landing.html', { 'profiles': profiles })
