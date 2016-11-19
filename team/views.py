from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from team.models import *

# Create your views here.
class memberList(ListView):
    model = Member
    template_name = ""

class memberDetail(DetailView):
    model = Member
    template_name= ""

