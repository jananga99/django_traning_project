from rest_framework import authentication
from firebase_admin import auth
from rest_framework.permissions import IsAuthenticated
import mysite.firebaseConfig

class BearerAuthentication(authentication.TokenAuthentication):
    keyword = ['token', 'bearer']

    def authenticate(self, request):
        authHeader = authentication.get_authorization_header(request).split()
        if not authHeader:
            return None
        if authHeader[0].lower().decode() not in self.keyword:
            return None
        if len(authHeader) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise authentication.exceptions.AuthenticationFailed(msg)
        elif len(authHeader) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise authentication.exceptions.AuthenticationFailed(msg)
        token = authHeader[1]
        decoded_token = auth.verify_id_token(token)
        return self.authenticate_credentials(decoded_token)

    def authenticate_credentials(self, token):
        user = auth.get_user(token['uid'])
        return (user, token)


class IsAuthenticatedSub(IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user)
