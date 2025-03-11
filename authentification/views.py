import json

from django.conf import settings


from typing import Protocol
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .decorators import user_not_authenticated
from .tokens import account_activation_token


from . import forms,geographic_data

from django.contrib.auth.views import LoginView
from django.contrib.messages import error
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.views import PasswordChangeView

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('homepage')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.email,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')






class CustomLoginView(LoginView):
    template_name = 'cvtheque/accueil.html'

    def form_invalid(self, form):
        # Ajouter un message d'erreur personnalisé
        error(self.request, _('Nom d\'utilisateur ou mot de passe incorrect. Veuillez réessayer.'))
        return self.render_to_response(self.get_context_data(form=form))



# Create your views here.
def inscription(request):
    form = forms.InscriptionForm()
    if request.method == 'POST':
        form = forms.InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #user.save()
            user.is_active = False
            user.save()
            #activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect(settings.LOGIN_REDIRECT_URL)

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
        # Préparer les données pour les cercles et les communes

    cercles_by_region = geographic_data.CERCLES_CHOICES

    communes_by_cercle = geographic_data.COMMUNES_CHOICES

    context = {
        "form": form,
        "cercles_by_region": json.dumps(cercles_by_region),
    "communes_by_cercle": json.dumps(communes_by_cercle),

    }


    return render(request, template_name="authentification/signup.html", context=context)

def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


class CustomPasswordChange(PasswordChangeView):
    form_class = forms.CustomPasswordChangeForm
    template_name = 'authentification/password_change_form.html'
    success_url = '/password-change-done/'
    def form_invalid(self, form):
        # Ajouter un message d'erreur personnalisé
        error(self.request, _('Nom d\'utilisateur ou mot de passe incorrect. Veuillez réessayer.'))
        return self.render_to_response(self.get_context_data(form=form))

