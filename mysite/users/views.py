import pyrebase
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import mysite.firebaseConfig as firebaseConfig



@csrf_exempt
@api_view(['POST'])
def signIn(request):
    data = JSONParser().parse(request)
    email = data.get('email')
    password = data.get('password')

    try:
        print(request.headers)
        # print(request.headers.Authorization)
        user = firebaseConfig.auth.sign_in_with_email_and_password(email, password)
        print(user)
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        response_data = {
            'session_id': session_id,
            'idToken': session_id,
            'email': email,
        }
        return Response(response_data)
    except Exception as e:
        message = "An error occurred while signing in. Please try again later."
        print(e)
        print(type(e))
        return Response({'error': message})


@csrf_exempt
@api_view(['POST'])
def signOut(request):
    try:
        del request.session['uid']
        return Response({'success': True})
    except Exception as e:
        print(e)
        print(type(e))
        return Response({'success': False})


@csrf_exempt
@api_view(['POST'])
def signUp(request):
    data = JSONParser().parse(request)
    email = data.get('email')
    password = data.get('password')
    name = data.get('username')
    try:
        user = firebaseConfig.auth.create_user_with_email_and_password(email, password)
        print(user)
        uid = user['localId']
        print(uid)
        response_data = {
            'uid': uid,
            'email': email,
        }
        return Response(response_data)
    except Exception as e:
        print(e)
        print(type(e))
        message = "Sign up error"
        return Response({'error': message})
