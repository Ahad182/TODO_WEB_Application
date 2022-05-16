from django.forms import ModelForm

from app.models import TODOMODEL


class TODOFORM(ModelForm):
    class Meta: 
        model = TODOMODEL
        fields = [
            'title',
            'status',
            'priority',

        ]