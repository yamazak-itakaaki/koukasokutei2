import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from koukasokutei2.koukasokutei2 import blog


logger = logging.getLogger(__name__)

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
        diary = get_object_or_404(blog, pk=self.kwargs['pk'])
        # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
        return self.request.user == diary.user

class BaseView(generic.TemplateView):
    template_name = "base.html"

class InquiryView(generic.FormView):
    template_name = "email_config.html"
    form_class = InquiryForm
    success_url = reverse_lazy('blog:email_config')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Blog
    template_name = 'blog_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Blog.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries