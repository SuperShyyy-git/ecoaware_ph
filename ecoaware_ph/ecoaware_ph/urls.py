from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),


    path('', TemplateView.as_view(template_name='home.html'), name='home'),


    path('users/', include('users.urls', namespace='users')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('campaigns/', include('campaigns.urls', namespace='campaigns')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)