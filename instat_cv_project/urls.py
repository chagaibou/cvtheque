"""
URL configuration for instat_cv_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cvtheque import views
from authentification.views import inscription,logout_view,CustomLoginView,activate,CustomPasswordChange
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CustomLoginView.as_view(

    ), name='accueil'),

    path("signup/",inscription,name='signup'),
    path("logout/",logout_view,name='logout'),
    path("menu", views.menu_view, name='menu'),
    path('password-change/',CustomPasswordChange.as_view(
    ),name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(
        template_name = "authentification/password_change_done.html"
    ),name ='password_change_done'),
    path('formations/', views.formations_view, name='formations'),
    path('formations/<int:formation_id>',views.remove_formation,name='remove-formation'),
    path('exp_professionnelles/', views.exp_professionnelles_view, name='exp_professionnelles'),
    path('exp_professionnelles/<int:exp_prof_id>', views.remove_exp_professionnelles, name='remove-exp-prof'),
    path('competences/',views. competences_view, name='competences'),
    path('competences/<int:competence_id>',views.remove_competence, name='remove-competence'),
    path('langues/', views.langues_view, name='langues'),
    path('langues/<int:langue_id>', views.remove_langue, name='remove-langue'),
path('activate/<uidb64>/<token>', activate, name='activate')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
