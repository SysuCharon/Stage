from django import forms
from news.models import News


class NewsForm(forms.Form):
    class Meta:
        model =  News
        field = ('title', 'content')
        widgets = {'title': forms.TextInput(),
                   "content":forms.TextInput()}