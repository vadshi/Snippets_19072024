from django.forms import ModelForm, ValidationError
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code']

    def clean_name(self):
        snippet_name = self.cleaned_data.get("name")
        if snippet_name is not None and len(snippet_name) > 3:
            return snippet_name
        raise ValidationError("Snippet's name is too short")