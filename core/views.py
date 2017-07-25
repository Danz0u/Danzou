from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from core.forms import *
from core.models import *


class IndexView(TemplateView):
    template_name = 'index.html'


class ThanksView(TemplateView):
    template_name = 'messages/thanks.html'


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
