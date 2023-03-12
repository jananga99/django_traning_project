import requests
from django.shortcuts import render
import pyrebase
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
    email = request.POST.get('email')
    pasw = request.POST.get('password')
    try:
        # if there is no error then signin the user with given email and password
        user = authe.sign_in_with_email_and_password(email, pasw)
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        return render(request, "Home.html", {"email": email})
    except Exception as e:
        message = "An error occurred while signing in. Please try again later."
        print(e)
        return render(request, "Signin.html", {"message": message})



def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Signin.html")


def signUp(request):
    return render(request, "Signup.html")


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('password')
    name = request.POST.get('name')
    try:
        # creating a user with the given email and password
        user = authe.create_user_with_email_and_password(email, passs)
        print(user)
        uid = user['localId']
        print(uid)
    except Exception as e:
        print(e)
        return render(request, "Signup.html")
    return render(request, "Signin.html")