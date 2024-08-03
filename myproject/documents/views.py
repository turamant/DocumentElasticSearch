from django.shortcuts import render, redirect
from .models import Document
from .tasks import index_document


def add_document(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        document = Document.objects.create(title=title, content=content)
        index_document.delay(document.id)
        return redirect('add_document')
    return render(request, 'add_document.html')
