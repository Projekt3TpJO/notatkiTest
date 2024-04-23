from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from aplikacjaNotatki.models import Note


class NotesView(ListView):
    queryset = Note.objects.all().order_by('urgency')
    paginate_by = 3
    context_object_name = 'notes'
    template_name = "notes/note/list.html"


def note_detail(request, year, month, day):
    note = get_object_or_404(Note, year=year, month=month, day=day)
    return render(request, "notes/note/detail.html", {'note': note})
