from django.contrib import admin
from . import models


class ExperiencesAdmin(admin.ModelAdmin):
    pass

class FormationAdmin(admin.ModelAdmin):
    pass

class CompetencesAdmin(admin.ModelAdmin):
    pass

class LangueAdmin(admin.ModelAdmin):
    pass



admin.site.register(models.ExperiencesProfessionnelles,ExperiencesAdmin)
admin.site.register(models.Formation,FormationAdmin)
admin.site.register(models.Competence,CompetencesAdmin)
admin.site.register(models.Langue,LangueAdmin)