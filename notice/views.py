from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from notice.models import *
from notice.forms import NoticeForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class noticeList(ListView):
    model=Notice
    template_name = "notice/noticeList.html"
    context_object_name = 'notice_list'

class noticeDetail(DetailView):
    model = Notice
    template_name = "notice/noticeDetail.html"
    context_object_name = "notice"

    def get(self, request, *args, **kwargs):
        self.object = Notice.objects.get(id=kwargs['id'])
        notice = Notice.objects.get(id=kwargs['id'])
        self.object.viewed()
        return self.render_to_response(self.get_context_data(notice=notice))

class noticeAdd(LoginRequiredMixin, CreateView):
    model = Notice
    template_name = "notice/noticeAdd.html"
    form_class = NoticeForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.save()
# Create your views here.
