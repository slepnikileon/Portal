from .models import Access
from django.views.generic import TemplateView, ListView
from django.db.models import Q


class Search(ListView):
    model = Access
    template_name = 'main/search.html'
    context_object_name = 'Access' #Используеться в Index.html
    extra_context = {'title': 'Главная страница'}
#    queryset = Access.objects.filter(Name__icontains='Amosov')

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
#        object_list = Access.objects.filter(Name__icontains=query)
        object_list = Access.objects.filter(Q(Name__icontains=query) | Q(EDRPOU__icontains=query) | Q(EMCI_Port__icontains=query))
        return object_list
    
#    def get_queryset(self):
#        return Access.objects.filter(Name__incontains=self.request.GET.get('q'))
#        return Access.objects.filter(Name__icontains='Amosov')
        
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['q'] = self.request.GET.get('q')
#        return context
