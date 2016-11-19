from django import forms
from notice.models import Notice


class NoticeForm(forms.Form):
    class Meta:
        model =  Notice
        field = ('title', 'content')
        widgets = {'title': forms.TextInput(),
                   "content":forms.TextInput()}
