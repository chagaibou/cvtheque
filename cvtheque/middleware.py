from django.http import HttpResponseForbidden
from django.conf import settings

class SuperuserRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Vérifiez si la requête est pour l'interface d'administration
        if request.path.startswith('/admin/'):
            # Vérifiez si l'utilisateur est authentifié et est un super administrateur
            if not request.user.is_authenticated or not request.user.is_superuser:
                return HttpResponseForbidden("Accès interdit : Vous devez être un super administrateur pour accéder à cette page.")

        response = self.get_response(request)
        return response
