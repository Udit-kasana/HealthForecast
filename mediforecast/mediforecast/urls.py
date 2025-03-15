
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('App.urls')),     
   

    path('main.html', include('App.urls')),
    # path('heart.html', include('App.urls')),
    # path('model.html', include('App.urls')),
    # path('manage.html', include('App.urls')),
    # path('wellBeing.html', include('App.urls')),
    # path('BMI.html', include('App.urls')),
    # path('Caloriecal.html', include('App.urls')),

    # path('home.html', include('App.urls')),
    # path('checkview', include('App.urls')),
]
