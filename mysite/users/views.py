import requests
from django.http import JsonResponse
from django.shortcuts import render
import pyrebase
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "apiKey": os.environ.get("API_KEY"),
    "authDomain": os.environ.get("AUTH_DOMAIN"),
    "databaseURL": os.environ.get("DATABASE_URL"),
    "projectId": os.environ.get("PROJECT_ID"),
    "storageBucket": os.environ.get("STORAGE_BUCKET"),
    "messagingSenderId": os.environ.get("MESSAGING_SENDER_ID"),
    "appId": os.environ.get("APP_ID"),
    "measurementId": os.environ.get("MEASUREMENT_ID")
}
# Initialising database,auth and firebase for further use
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def signIn(request):
    return render(request, "Signin.html")


def home(request):
    return render(request, "Home.html")


def postsignIn(request):
    print("Start of post request")
    print(request.POST['email'])
    email = request.POST.get('email')
    pasw = request.POST.get('password')
    try:
        # if there is no error then signin the user with given email and password
        user = authe.sign_in_with_email_and_password(email, pasw)
        print(user)
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        response_data = {
            'session_id': session_id,
            'email': email,
        }
        return JsonResponse(response_data)
        # return render(request, "Home.html", {"email": email})
    except Exception as e:
        message = "An error occurred while signing in. Please try again later."
        print(e)
        return JsonResponse({'error': message})
        # return render(request, "Signin.html", {"message": message})


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Signin.html")


def signUp(request):
    return render(request, "Signup.html")

def postsignUp(request):
    print("In begiuning")
    data = JSONParser().parse(request)
    print(data)
    email = data.get('email')
    passs = data.get('password')
    name = data.get('username')
    print(email, passs, name)
    try:
        # creating a user with the given email and password
        user = authe.create_user_with_email_and_password(email, passs)
        print(user)
        uid = user['localId']
        print(uid)
        response_data = {
            'uid': uid,
            'email': email,
        }
        return JsonResponse(response_data)
    except Exception as e:
        print(e)
        message = "Sign up error"
        return JsonResponse({'error': message})
        # return render(request, "Signup.html")
    # return render(request, "Signin.html")
