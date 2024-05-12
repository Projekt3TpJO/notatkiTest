from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from aplikacjaNotatki.forms import NoteForm
from aplikacjaNotatki.models import Note


class NotesView(ListView):
    queryset = Note.objects.all().order_by('urgency')
    paginate_by = 4
    context_object_name = 'notes'
    template_name = "notes/note/list.html"


def note_detail(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, "notes/note/detail.html", {'note': note})


def note_create(request):
    if request.method == "POST":
        note_form = NoteForm(data=request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.save()
    note_form = NoteForm()
    return render(request, "notes/note/create.html", {'note_form': note_form})
