from django.urls import path
from .form import Search
from .views import HomePageView, Index
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('',views.index, name='home'),
    #path('about-us',views.about, name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('index/', Index.as_view(), name='index'),
    path('search/', Search.as_view(), name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
]
