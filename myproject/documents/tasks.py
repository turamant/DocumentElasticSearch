from celery import shared_task
from elasticsearch import Elasticsearch
from .models import Document

es = Elasticsearch(['http://elasticsearch:9200'])

@shared_task
def index_document(doc_id):
    document = Document.objects.get(id=doc_id)
    es.index(index='documents', id=doc_id, body={
        'title': document.title,
        'content': document.content,
        'date': document.date,
    })
