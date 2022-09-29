import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import InquiryForm
# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "base.html"

class InquiryView(generic.FormView):
    template_name="inquiry.html"
    form_class = InquiryForm
