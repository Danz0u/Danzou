from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from core.forms import *
from core.models import *


class ThanksView(TemplateView):
    template_name = 'messages/thanks.html'


class IndexView(ListView):
    model = Anime
    template_name = "index.html"

    def get_queryset(self, **kwargs):
        return Anime.objects.all().order_by('-created_at')[:6]


class AnimeListView(ListView):
    model = Anime
    template_name = "animes.html"

    def get_queryset(self, **kwargs):
        return Anime.objects.all().order_by('title')


class AnimeSearchList(AnimeListView):
    paginate_by = 3

    def get_queryset(self):
        queryset = super(AnimeSearchList, self).get_queryset()

        query = self.request.GET.get('search_box')

        if query:
            query_list = query.split()
            return queryset.filter(title__contains=query).order_by('title')
        return queryset


class AnimeDetailView(DetailView):
    model = Anime
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super(AnimeDetailView, self).get_context_data(**kwargs)
        return context


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
