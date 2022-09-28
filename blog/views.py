
from django.views import generic

from .forms import InquiryForm

# Create your views here.
class loginView(generic.TemplateView):
class IndexView(generic.TemplateView):
    template_name = "base.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
