from email import message
from django import forms
import os
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='氏名', max_length=30)
    email = forms.EmailField(label='メール')
    css = forms.CharField(label='件名', max_length=30)
    text = forms.CharField(label='本文', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '氏名をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['css'].widget.attrs['class'] = 'form-control'
        self.fields['css'].widget.attrs['placeholder'] = '件名をここに入力してください。'

        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['placeholder'] = '本文をここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        css = self.cleaned_data['css']
        text = self.cleaned_data['text']

        subject = 'お問い合わせ{}'.format(css)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, text)

        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()