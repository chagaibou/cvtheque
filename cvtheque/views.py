from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from . import forms,models

@login_required
def menu_view(request):


    return render(request, "cvtheque/menu.html")


# def contact_view(request):
#     return render(request,template_name="cvtheque/contact.html")

def formations_view(request):
    formations = models.Formation.objects.filter(candidat=request.user)
    form = forms.FormationForm()
    if request.method == 'POST':
        form = forms.FormationForm(request.POST,request.FILES)
        if form.is_valid():
            formation = form.save(commit=False)
            formation.candidat = request.user
            formation.save()
            return redirect('menu')

    context = {
        'form':form,
        'formations': formations,

    }

    return render(request,template_name="cvtheque/formations.html",context=context)

def remove_formation(request,formation_id):
    models.Formation.objects.filter(id = formation_id).delete()

    return redirect('menu')
def edit_formation(request,formation_id):
    formation = get_object_or_404(models.Formation,id=formation_id)
    edit_form =  forms.FormationForm(instance=formation)
    delete_form = forms.DeleteFormation()
    if request.method == 'POST':
        if 'edit_formation' in request.POST:
            edit_form = forms.FormationForm(request.POST,instance=formation)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('accueil')
            if 'delete_formation' in request.POST:
                delete_form = forms.DeleteFormation(request.POST)
                if delete_form.is_valid():
                    formation.delete()
                    return redirect('accueil')

    context = {
        'edit_form':edit_form,
        'delete_form':delete_form
    }
    return render(request,'cvtheque/edit_formations.html',context=context)
def exp_professionnelles_view(request):
    exp_prof = models.ExperiencesProfessionnelles.objects.filter(candidat=request.user)
    form = forms.ExperiencesProfessionellesForm()
    if request.method == 'POST':
        form = forms.ExperiencesProfessionellesForm(request.POST, request.FILES)
        if form.is_valid():
            experience_professionnelle = form.save(commit=False)
            experience_professionnelle.candidat = request.user
            experience_professionnelle.save()
            return redirect('menu')
    context = {
        'form': form,
        'exp_prof':exp_prof
    }

    return render(request, template_name="cvtheque/exp_professionnelles.html",context=context)

def remove_exp_professionnelles(request,exp_prof_id):
    models.ExperiencesProfessionnelles.objects.filter(id = exp_prof_id).delete()
    return redirect('menu')
def competences_view(request):
    competences = models.Competence.objects.filter(candidat=request.user)
    form = forms.CompetenceForm()
    if request.method == 'POST':
        form = forms.CompetenceForm(request.POST)
        if form.is_valid():
            competence = form.save(commit=False)
            competence.candidat = request.user
            competence.save()
            return redirect('menu')
    context = {
        'form': form,
        'competences' : competences
    }
    return render(request, template_name="cvtheque/competences.html",context=context)

def remove_competence(request,competence_id):
    models.Competence.objects.filter(id=competence_id).delete()
    return redirect('menu')

def langues_view(request):
    langues = models.Langue.objects.filter(candidat=request.user)
    form = forms.LangueForm()
    if request.method == 'POST':
        form = forms.LangueForm(request.POST)
        if form.is_valid():
            langue = form.save(commit=False)
            langue.candidat = request.user
            langue.save()
            return redirect('menu')
    context = {
        'form': form,
        'langues' : langues
    }

    return render(request, template_name="cvtheque/langues.html",context=context)

def remove_langue(request,langue_id):
    models.Langue.objects.filter(id=langue_id).delete()
    return redirect('menu')


from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email from Django.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['chagaiboututo@gmail.com']  # Remplacez par votre adresse email

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Test email sent successfully.')


