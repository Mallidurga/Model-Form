from pyexpat import model
from django import forms
from app.models import *
#from django.utils.translation import gettext_lazy as g
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['topic_name','name']
        #widgets={'name':forms.PasswordInput}
        #labels={'name':g('Changed'),'topic_name':g('again changed')}
        #help_texts={'name':g('enter ur name')}