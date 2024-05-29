from django import forms

from aplikacjaNotatki.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        URGENCY_CHOICES = (
            ('High', 'High'),
            ('Low', 'Low'),
        )
        title = forms.CharField(max_length=100)
        description = forms.Textarea
        urgency = forms.ChoiceField(choices=URGENCY_CHOICES)
