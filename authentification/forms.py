from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _


class InscriptionForm( UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'first_name', 'last_name','date_de_naissance',
            'genre', 'situation_matrimoniale', 'nationalite',
            'email', 'telephone', 'region', 'cercle', 'commune','residence_legale'
        )
        labels = {
            "email": "E-mail",
            "last_name": "Nom",
            "first_name": "Prénom",
            "password1": "Mot de passe",
            "genre": "Genre",
            "situation_matrimoniale": "Situation Matrimoniale",
            "nationalite": "Nationalité",
            "telephone": "Téléphone",
            "region": "Région",
            "residence_legale" : 'Résidence Légale'
        }

        widgets = {
            'date_de_naissance': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'region': forms.Select(attrs={'id': 'id_region'}),
            'cercle': forms.Select(attrs={'id': 'id_cercle'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmation du mot de passe"
        self.fields['password2'].help_text = _(
            "Entrez le même mot de passe qu'auparavant, pour vérification."
        )
        self.fields['date_de_naissance'].widget.attrs.update({'class': 'form-control'})
        self.fields['region'].widget.attrs.update({'class': 'form-control'})
        self.fields['cercle'].widget.attrs.update({'class': 'form-control'})
        self.fields['commune'].widget.attrs.update({'class': 'form-control '})


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Ancien mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label="Confirmer le nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )




