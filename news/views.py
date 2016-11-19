from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from news.models import *
from news.forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class newsList(ListView):
    model=News
    template_name = "news/newsList.html"
    context_object_name = 'news_list'

class newsDetail(DetailView):
    model = News
    template_name = "news/newsDetail.html"
    context_object_name = "news"

    def get(self, request, *args, **kwargs):
        self.object = News.objects.get(id=kwargs['id'])
        news = News.objects.get(id=kwargs['id'])
        self.object.viewed()
        return self.render_to_response(self.get_context_data(news=news))

class newsAdd(LoginRequiredMixin, CreateView):
    model = News
    template_name = "news/newsAdd.html"
    form_class = NewsForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.save()

