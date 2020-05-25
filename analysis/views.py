from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader 
from analysis.models import StudentGrades, Course


# Application views
def login(request):

    template = loader.get_template('analysis/login.html')

    return HttpResponse(template.render(None, request))

def dashboard(request):

    template = loader.get_template('analysis/dashboard.html')
    return HttpResponse(template.render(None, request))

def charts(request):

     studentInfo = StudentGrades.objects.all()
     courseInfo = Course.objects.all()
     
  
     print(studentInfo)
     scorelist, courselist = [], []
     for element in studentInfo:
        scorelist.append(element.score)
     
     for element in courseInfo:
          courselist.append(element.couse_id)
     print(courselist)

     args = {'scorelist': scorelist, 'courselist': courselist}
     template = loader.get_template('analysis/charts.html')


     return HttpResponse(template.render(args, request))