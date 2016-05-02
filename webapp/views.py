from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Mobile
import jieba

# Create your views here.
def index(request):
    cnt = [0,0,0,0,0,0,0]
    cnt[0] = len(Mobile.objects.filter(price__range=(0,1000)))
    cnt[1] = len(Mobile.objects.filter(price__range=(1000,2000)))
    cnt[2] = len(Mobile.objects.filter(price__range=(2000,3000)))
    cnt[3] = len(Mobile.objects.filter(price__range=(3000,4000)))
    cnt[4] = len(Mobile.objects.filter(price__range=(4000,5000)))
    cnt[5] = len(Mobile.objects.filter(price__range=(5000,6000)))
    cnt[6] = len(Mobile.objects.filter(price__gte=6000))
    cntListDate = [0,0,0,0,0,0,0]
    cntListDate[0] = Mobile.objects.filter(listDate__contains='2016').count()
    cntListDate[1] = Mobile.objects.filter(listDate__contains='2015').count()
    cntListDate[2] = Mobile.objects.filter(listDate__contains='2014').count()
    cntListDate[3] = Mobile.objects.filter(listDate__contains='2013').count()
    cntListDate[4] = Mobile.objects.filter(listDate__contains='2012').count()
    cntListDate[5] = Mobile.objects.filter(listDate__contains='2011').count()
    cntListDate[6] = Mobile.objects.all().count() - (cntListDate[0]+cntListDate[1]+cntListDate[2]+cntListDate[3]+cntListDate[4]+cntListDate[5])
    return render(request,'index.html',{'cnt': cnt, 'cntListDate': cntListDate})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def search(request):
    sea = request.GET['search']
    s = jieba.lcut(sea,cut_all=False)
    while ' ' in s:
        s.remove(' ')
    results = []
    for ss in s:
        keywords = Mobile.objects.filter(keywords__icontains=ss)
        results.append(keywords)
    res = list(set(results[0]).union(*results[1:]))
    products = {}
    for pro in res:
        products[pro] = pipeidu(pro.keywords,s)
    pros = sorted(products.iteritems(),key=lambda products:products[1],reverse=True)
    len_list = len(pros)
    return render(request,'results.html',{'pros':pros,'len_list':len_list})

def pipeidu(str_keywords,list_fenci):
    cnt = 0
    for fenci in list_fenci:
        if fenci in str_keywords:
            cnt += 1
    return cnt

def addCompare(request):
    id_list = request.GET.getlist('mobile')
    detail_list = []
    print id_list
    for id in id_list:
        details = Mobile.objects.get(skuid=id)
        detail_list.append(details)
    return render(request,'cmps.html',{'detail_list':detail_list})
