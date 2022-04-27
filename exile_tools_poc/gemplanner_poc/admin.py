from django.contrib import admin

# Register your models here.
from .models import POESkillGem, POECharacterClass

admin.site.register(POESkillGem)
admin.site.register(POECharacterClass)
