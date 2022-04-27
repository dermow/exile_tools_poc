from django.http import HttpResponse
from django.template import loader

from .models import POESkillGem

def index(request):
    gemlist = POESkillGem.objects.all()
    template = loader.get_template('gemplanner_poc/index.html')
    context = {
        'gemlist': gemlist,
    }
    return HttpResponse(template.render(context, request))
