from django.shortcuts import render
import numpy as np
from sklearn.preprocessing import StandardScaler
from django.conf import settings


# Create your views here.
from joblib import load
classifier = load("./savedmodels/diabetes.joblib")

model1=load("./savedmodels/heart.joblib")
# model=load("./savedmodels/breastcancer.joblib")
mode=load("./savedmodels/breastcancer.joblib")

# from .models import YourModel
# s=".html"
def Home(request):
    return render(request,'index.html')
def BC(request):
    if request.method=='POST':
        id=request.POST['id']
        diagnosis=request.POST['diagnosis']
        radius_mean=request.POST['radius_mean']
        texture_mean=request.POST['texture_mean']
        perimeter_mean=request.POST['perimeter_mean']
        area_mean=request.POST['area_mean']
        smoothness_mean=request.POST['smoothness_mean']
        compactness_mean=request.POST['compactness_mean']
        concavity_mean=request.POST['concavity_mean']
        concave_points_mean=request.POST['concave points_mean']
        symmetry_mean=request.POST['symmetry_mean']
        fractal_dimension_mean=request.POST['fractal_dimension_mean']
        radius_se=request.POST['radius_se']
        texture_se=request.POST['texture_se']
        perimeter_se=request.POST['perimeter_se']
        area_se=request.POST['area_se']
        smoothness_se=request.POST['smoothness_se']
        compactness_se=request.POST['compactness_se']
        concavity_se=request.POST['concavity_se']
        concave_points_se=request.POST['concave points_se']
        symmetry_se=request.POST['symmetry_se']
        fractal_dimension_se=request.POST['fractal_dimension_se']
        radius_worst=request.POST['radius_worst']
        texture_worst=request.POST['texture_worst']
        perimeter_worst=request.POST['perimeter_worst']
        area_worst=request.POST['area_worst']
        smoothness_worst=request.POST['smoothness_worst']
        compactness_worst=request.POST['compactness_worst']
        concavity_worst=request.POST['concavity_worst']
        concave_worst=request.POST['concave_worst']
        symmetry_worst=request.POST['symmetry_worst']
        fractal_dimension_worst=request.POST['fractal_dimension_worst']
        input_data = (id, diagnosis,radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_worst,symmetry_worst,fractal_dimension_worst)

# Change the input data to a numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # Reshape the numpy array as wwe aree predecting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        prediction = mode.predict(input_data_reshaped)
        

        if (prediction[0]== 0):
          prediction='The Breast cancer is Maligant'

        else:
           prediction= 'The Breast cancer is Benign' 
        
        return render(request, 'bc.html', {'result' : prediction})
    return render(request,'bc.html')
def index(request):
    dict={
        "wellbeing":"wellBeing",
        "bmi":"BMI",
        "calorie":"Caloriecal",
        "doctors":"Doctors",
        "diabetes":"main",
        "heart":"heart",
        "breast":"breast",
        "appointment":"manage",



    }
    if request.method=="POST":
        # query=request.GET.get('query')
        # results=YourModel.objects.filter(title__icontains=query)
        data=request.POST['search']
        if data in dict.keys():
            # s=dict[data]+".html"
            return render (request,f'{dict[data]}.html')
        
    
    return  render(request,'index.html')

def model(request):
    return  render(request,'model.html')
def Doctors(request):
    return render(request,'Doctors.html')

def Predictor(request):
    if request.method=='POST':
        preg=request.POST['preg']
        glucose=request.POST['glu']
        BP=request.POST['BP']
        st=request.POST['ST']
        Insulin=request.POST['Insulin']
        Bmi=request.POST['BMI']
        Dpf=request.POST['DPF']
        Age=request.POST['Age']
        input_data=(preg,glucose,BP,st,Insulin,Bmi,Dpf,Age)
        inputdata_asnumpy=np.asarray(input_data)
        input_data_reshaped = inputdata_asnumpy.reshape(1,-1)
        # scalar=StandardScaler()
        # std_data =scalar.fit_transform(input_data_reshaped)
        prediction=classifier.predict(input_data_reshaped)
        if (prediction [0] == 0):
            prediction='The person is not diabetic'
        else:
            prediction='The person is diabetic'
        return render(request, 'diabetes.html', {'result' : prediction})
    return render(request, 'diabetes.html')

def predict(request):
    if request.method=='POST':
        Age=request.POST['Age']
        sex=request.POST['Sex']
        CP=request.POST['CP']
        Trestbps=request.POST['trestbps']
        Chol=request.POST['chol']
        Fbs=request.POST['fbs']
        Restecg=request.POST['restecg']
        Thalach=request.POST['thalach']
        Exang=request.POST['exang']
        Oldpeak=request.POST['oldpeak']
        Slope=request.POST['slope']
        ca=request.POST['ca']
        Thal=request.POST['thal']

        input_data=(Age,sex,CP,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,ca,Thal)
        inputdata_asnumpy=np.asarray(input_data,dtype=np.float64)
        input_data_reshaped = inputdata_asnumpy.reshape(1,-1)
    # scalar=StandardScaler()
    # std_data =scalar.fit_transform(input_data_reshaped)
        prediction=model1.predict(input_data_reshaped)
        if (prediction[0]== 0):
            prediction='The Person does not have a Heart disease'
        else:
            prediction ='The person has Heart disease'
        return render(request, 'heart.html', {'result' : prediction})
    return render(request, 'heart.html')


def wellbeing(request):
    return  render(request,'wellBeing.html')
def Caloriecal(request):
    return  render(request,'Caloriecal.html')
def BMI(request):
    return  render(request,'BMI.html')
from django.shortcuts import render, redirect
from App.models import Room, Message,Appoint
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        return HttpResponse("The room you types not exist")

        # new_room = Room.objects.create(name=room)
        # new_room.save()
        # return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
# from django.contrib.auth.models import App
import random
num = random.random()
from django.contrib import messages
def Appointment(request):
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Phone=request.POST['phone']
        Doctor=request.POST['doc']
        Date=request.POST['date']
        Time=request.POST['time']
        num=random.randint(1001,9999)
        if Appoint.objects.filter(Email=Email, Date=Date).exists():
            str=f'{Name} you have already registered  with the Email id{Email} on the date{Date}'
            # messages.warning(request,'you have already registered')
        else:
            appointment=Appoint.objects.create(Name=Name,Email=Email,Phone=Phone,Date=Date,Time=Time,Doctor=Doctor)
            appointment.save()
            str=f'{Name} your appointment has been scheduled with {Doctor} on {Date} at time{Time} and your MRN ID is{num}'
        return render(request, 'manage.html', {'result' : str})
        # return HttpResponse('Message sent successfully')

        
    return  render(request,'manage.html')