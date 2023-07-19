from django.shortcuts import render
from app.models import *
from app.forms import *
# Create your views here.
from django.http import HttpResponse

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        STFO=TopicForm(request.POST)
        if STFO.is_valid():
            topic_name=STFO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()

        return HttpResponse('<center><h1>Data is inserted to the Django Form</h1></center>')
    
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    TFO=Topic.objects.all()
    WFO=WebpageForm()
    w={'WFO':WFO}
    if request.method=='POST':
        TO=Topic.objects.get(topic_name=topic_name)

    


    return render(request,'insert_webpage.html',w)


def insert_accessrecord(request):
    ARFO=AccessRecordForm()
    a={'ARFO':ARFO}
    if request.method=='POST':
        WO=Webpage

    return render(request,'insert_accessrecord.html',a)
