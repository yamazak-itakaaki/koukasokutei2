import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "base.html"
