# encoding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import Template, RequestContext, loader
from django.forms import fields
from django.core.mail import send_mail

import fdyouth.models
import account.models
import keywords.models

import traceback

import re

from fdyouth.forms import *

def index(request):
    return render_to_response('index.html',{})

def overview(request):
    view_type = request.REQUEST.get('type')
    if (view_type == 'academy'):
        name = '学术思想中心'
    if (view_type == 'life'):
        name = '生活资讯'
    if (view_type == 'news'):
        name = '校园新闻'
    account_list = account.models.list.objects.filter(type=view_type)
    context={
        'type': name,
        'image': view_type,
        'account_list': account_list
    }
    return render_to_response('overview.html',context)

def about(request):
    return render_to_response('about.html', {})

def contact(request):
    return render_to_response('contact.html', {})

def add(request):
    view_type = request.REQUEST.get('type')
    if (view_type == 'academy'):
        name = '学术思想中心'
    if (view_type == 'life'):
        name = '生活资讯'
    if (view_type == 'news'):
        name = '校园新闻'
    return render_to_response('add.html', {'view_type':view_type, 'name':name},context_instance=RequestContext(request))

def add_academy(request):
    return render_to_response('add_academy.html', {}, context_instance=RequestContext(request))

def add_life(request):
    return render_to_response('add_life.html', {}, context_instance=RequestContext(request))

def add_news(request):
    return render_to_response('add_news.html', {}, context_instance=RequestContext(request))

def add_statu(request):
    view_type=request.REQUEST.get('type')
    if (view_type == 'academy'):
        upload_form = academy_form(request.POST, request.FILES)
        try:
            upload_form.save()
        except:
            traceback.print_exc()
            pass
        return HttpResponseRedirect('add_academy.html')

    if (view_type == 'life'):
        upload_forms = life_form(request.POST, request.FILES)
        try:
            upload_forms.save()
        except:
            traceback.print_exc()
            pass
        return HttpResponseRedirect('add_life.html')

    if (view_type == 'news'):
        upload_news = news_form(request.POST, request.FILES)
        try:
            upload_news.save()
        except:
            traceback.print_exc()
            pass
        return HttpResponseRedirect('add_news.html')

def getKwargs(data={}):
    kwargs = {}
    if (data['title']):
        kwargs['title__icontains'] = data['title']
    if (data['keyword']):
        kwargs['keyword__icontains'] = data['keyword']
    if (data['begin_date']):
        kwargs['date__gte'] = data['begin_date']
    if (data['end_date']):
        kwargs['date__lte'] = data['end_date']
    if ('start_issue' in data.keys() and data['start_issue']):
        kwargs['issue__gte']=data[start_issue]
    if ('end_issue' in data.keys() and data['end_issue']):
        kwargs['issue__lte'] = data['end_issue']
    if ('author' in data.keys() and data['author']):
        kwargs['author__icontains'] = data['author']
    if ('place' in data.keys() and data['place']):
        kwargs['place'] = data['place']
    if ('field' in data.keys() and data['field']):
        kwargs['field__icontains'] = data['field']
    return kwargs

def search_result(request):
    view_type = request.REQUEST.get('type')
    result={}
    seq = getKwargs(request.REQUEST)
    if (seq):
        if (view_type == 'news'):
            result = news.objects.filter(**seq)
        if (view_type == 'life'):
            result = overseas.objects.filter(**seq)
        if (view_type == 'academy'):
            result = academy.objects.filter(**seq)
    return render_to_response('search_result.html', {'view_type':view_type, 'result':result}, context_instance=RequestContext(request)) 

def search_academy(request):
    return render_to_response('search_academy.html', {}, context_instance=RequestContext(request))

def search_life(request):
    return render_to_response('search_life.html', {}, context_instance=RequestContext(request))

def search_news(request):
    return render_to_response('search_news.html', {}, context_instance=RequestContext(request))

def search(request):
    view_type = request.REQUEST.get('type')
    if (view_type == 'academy'):
        name = '学术思想中心'
    if (view_type == 'life'):
        name = '生活资讯'
    if (view_type == 'news'):
        name = '校园新闻'
    return render_to_response('search.html',{'view_type':view_type, 'name':name},context_instance=RequestContext(request))

def details(request):
    view_type = request.REQUEST.get('type')
    seq_id = request.REQUEST.get('id')
    if (view_type == 'academy'):
        result = academy.objects.filter(id = seq_id)
    if (view_type == 'life'):
        result = overseas.objects.filter(id = seq_id)
    if (view_type == 'news'):
        result = news.objects.filter(id = seq_id)
    res = result[0]
    path = str(res.article)
    if re.match(r"http", path):
        from_file = False
    else:
        from_file = True
    if (from_file):
        res.article.open()
        data = res.article.read().split('\n')[4:]
        res.article.close()
    else:
        data = ""
    return render_to_response('details.html', {'from_file':from_file, 'file':result[0], 'view_type':view_type,'data':data},context_instance=RequestContext(request))

def download(request):
    view_type = request.REQUEST.get('type')
    seq_id = request.REQUEST.get('id')
    if (view_type == 'academy'):
        result = academy.objects.filter(id = seq_id)
    if (view_type == 'life'):
        result = overseas.objects.filter(id = seq_id)
    if (view_type == 'news'):
        result = news.objects.filter(id = seq_id)
    result = result[0]
    result.article.open()
    data = result.article.read()
    result.article.close()
    file_name = str(result.article.url) + ".txt"
    response = HttpResponse(data, content_type='text/plain')
    response['Content-Disposition'] = "attachment; filename={}".format(file_name)
    return response

def sendmail(request):
    pass
