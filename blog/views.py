import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import InquiryForm
# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "base.html"

class InquiryView(generic.FormView):
    template_name="inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('blog:inquiry')

    def form_valid(self, form):
       form.send_email()
       logger.info('Inquiry sent by {}'.format(form.cleande_data['name']))
       return super().form_valid(form)