from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from Feedback.models import Question
from Feedback.models import Tag
from Feedback.models import Status
# Create your views here.


def index(request):
    qustion_list = Question.objects.all()
    return render(request, 'Feedback/index.html', {"qustion_list": qustion_list})


def detail(request, question_id):
    return render(request, 'Feedback/detail.html', {})


def post(requst, method):
    return render(requst, 'Feedback/post.html', {})