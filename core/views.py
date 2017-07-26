from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView

from core.forms import *
from core.models import *


class ThanksView(TemplateView):
    template_name = 'messages/thanks.html'


class IndexView(ListView):
    model = Anime
    template_name = "index.html"

    def get_queryset(self, **kwargs):
        return Anime.objects.all().order_by('-created_at')[:6]


class RelatedBugsView(CreateView):
    model = RelatedBugs
    template_name = "report.html"
    form_class = RelatedBugForm
    success_url = '/thanks/'

    def get_context_data(self, **kwargs):
        context = super(RelatedBugsView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(RelatedBugsView, self).form_valid(form)
