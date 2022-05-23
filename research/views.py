from django.shortcuts import render
from django.views.generic import ListView
from .models import Research


class ResearchView(ListView):

    model = Research

    context_object_name = "Research"
