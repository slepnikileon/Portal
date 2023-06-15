from django.shortcuts import render
from .models import Access
from django.views.generic import TemplateView, ListView, View


class HomePageView(TemplateView):
    template_name = 'main/start.html'
#   template_name = 'registration/login.html'
 

class Index(TemplateView):
    template_name = 'main/index.html'





#def index(request):
#    Accesses = Access.objects.all()
#    return render(request,'main/index.html', {'title:': 'Главная страница', 'Access':Accesses})

#class HomePageView(ListView):
#    template_name = 'main/index.html'

#def about(request):
#    return render(request,'main/about.html') 


