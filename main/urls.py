from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500

urlpatterns = [
    path('', include('home.urls'), name='home-urls'),
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls'), name='portfolio_urls'),
    path('accounts/', include('allauth.urls')),
]
handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
