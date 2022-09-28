from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(label='氏名', max_length=30)
    email = forms.EmailField(label='メール')
    subject = forms.CharField(label='件名', max_length=30)
    text = forms.CharField(label='本文', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '氏名をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['placeholder'] = '件名をここに入力してください。'

        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['placeholder'] = '本文をここに入力してください。'