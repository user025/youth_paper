# encoding=UTF-8

from django.shortcuts import render, render_to_response, RequestContext

from django.core.mail import send_mail
from subscribe.models import *

import traceback

def subscribe(request):
    view_type = request.REQUEST.get('type')
    if (view_type == 'academy'):
        name = '学术思想中心关键词'
    if (view_type == 'life'):
        name = '生活资讯关键词'
    if (view_type == 'news'):
        name = '校园新闻关键词'
    keyword_list = keywords.objects.filter(type=view_type)
    return render_to_response('subscribe.html', {'name':name,'keyword_list':keyword_list, 'view_type':view_type}, context_instance=RequestContext(request))

def subscribe_statu(request):
    view_type = request.REQUEST.get('type')
    user_email = request.REQUEST.get('email')
    word_list = request.POST.getlist('words')
    statu = True
    try:
    	send_mail('欢迎订阅复指数', '资讯全掌握，尽在复指数', 'fudanpoint@sina.com', [user_email])
    except:
	traceback.print_exc()
    try:
        user_exist = user.objects.filter(email=user_email)
        if (len(user_exist) > 0):
            user_exist[0].keyword = ' '.join(word_list)
            user_exist[0].save()
        else:
            new_user = user(email=user_email, keyword=' '.join(word_list), type=view_type)
            new_user.save()

        return render_to_response('subscribe_statu.html',{'statu':statu, 'user':user_email, 'view_type':view_type}, context_instance=RequestContext(request))
    except:
        statu = False
        traceback.print_exc()
        return render_to_response('subscribe_statu.html', {'statu':statu, 'view_type':view_type}, context_instance=RequestContext(request))
