from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Note


class NotesView(ListView):
    queryset = Note.objects.all().filter(urgency=2).order_by('-urgency')
    paginate_by = 5
    context_object_name = 'notes'
    template_name = "notes/note/list.html"


def note_detail(request, year, month, day):
    note = get_object_or_404(Note, urgency=request.GET['urgency'], year=year, month=month, day=day)
    return render(request, "notes/note/detail.html", {'note': note})
