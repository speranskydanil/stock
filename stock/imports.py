import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.db.models import Count
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from stock.models import Message
from stock.forms import ContactForm, SignUpForm
from blog.models import Article, Category, Like
from blog.forms import ArticleForm

def paginated(objects, request):
    paginator = Paginator(objects, 20)
    page = request.GET.get('page')

    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

