# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from web.models import *
from django.utils.translation import ugettext_lazy as _
from dartgolive.settings import MEDIA_URL, STATIC_URL
from django.template import RequestContext
from random import randint
import urllib2
from time import sleep

def launchProject(request):

    try:
        project = get_object_or_404(Project, active=True)
        project.golive = True
        project.save()
    except:
        project = None
    print "Project selected: %s"%(project)

    return HttpResponse("Project %s launched!"%(project))

def checkLaunch(request):

    try:
        project = Project.objects.get(golive=True)

    except:
        project = None
    print "Project selected: %s"%(project)

    if project:
        result = urllib2.urlopen(project.getURI)   
    
        return render_to_response("launch.html",{"GO":True,"project":project,"STATIC_URL":STATIC_URL})

    else:
        project = get_object_or_404(Project, active=True)
        return render_to_response("launch.html",{"GO":False,"project":project})
