from django.contrib.auth.views import LoginView

class AuthView(LoginView):
    template_name = 'authorization.html'
    redirect_authenticated_user = '/calendar/'