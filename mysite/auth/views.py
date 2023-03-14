from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import mysite.firebaseConfig as firebaseConfig


@csrf_exempt
@api_view(['POST'])
def signIn(request):
    """
    Sign in user using pyrebase.auth with email and password
    :param request: Request
    :return Response: rest_framework.response
    """
    data = JSONParser().parse(request)
    email = data.get('email')
    password = data.get('password')

    try:
        user = firebaseConfig.auth.sign_in_with_email_and_password(email, password)
        response_data = {
            'idToken': user['idToken'],
            'email': email,
        }
        return Response(response_data)
    except Exception as e:
        message = "An error occurred while signing in. Please try again later."
        return Response({'error': message})


@csrf_exempt
@api_view(['POST'])
def signOut(request):
    """
    Signs out a user
    :param request: Request
    :return Response: rest_framework.response
    """
    return Response({'success': True})


@csrf_exempt
@api_view(['POST'])
def signUp(request):
    """
    Signs up a new user using pyrebase.auth with email and password
    :param request: Request
    :return Response: rest_framework.response
    """
    data = JSONParser().parse(request)
    email = data.get('email')
    password = data.get('password')
    name = data.get('username')
    try:
        user = firebaseConfig.auth.create_user_with_email_and_password(email, password)
        uid = user['localId']
        response_data = {
            'uid': uid,
            'email': email,
        }
        return Response(response_data)
    except Exception as e:
        message = "Sign up error"
        return Response({'error': message})
