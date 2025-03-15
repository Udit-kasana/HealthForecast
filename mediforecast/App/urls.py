from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
     path('index.html', views.index, name = 'index'),
     path('bc.html', views.BC, name = 'BC'),
     path('diabetes.html', views.Predictor, name = 'Predictor'),
     # path('index.html', views.Home, name = 'Home'),
     path('heart.html', views.predict, name = 'predict'),
     path('model.html',views.model,name='model'),
     path('manage.html',views.Appointment,name='Appointment'),
     path('wellBeing.html',views.wellbeing,name='wellBeing'),
     path('BMI.html',views.BMI,name='BMI'),
     path('Doctors.html', views.Doctors, name='Doctors'),
     path('Caloriecal.html',views.Caloriecal,name='Caloriecal'),
     path('home.html',views.home,name='home'),
     path('<str:room>/', views.room, name='room'),
     path('checkview', views.checkview, name='checkview'),
     path('send', views.send, name='send'),
     path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
     # path('admin/', admin.site.urls),
     path('', views.index, name = 'index'),
]
